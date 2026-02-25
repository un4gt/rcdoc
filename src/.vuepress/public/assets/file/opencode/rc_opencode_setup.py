# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///

from __future__ import annotations

import argparse
import copy
import datetime as _dt
import json
import os
import re
import secrets
import shutil
import sys
import tempfile
import urllib.error
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


TEMPLATE_ZIP_URL = "https://docs.right.codes/assets/file/opencode/QuickConfiguration.zip"


@dataclass(frozen=True)
class ProviderSpec:
    provider_id: str
    label: str
    recommended_base_url: str
    headers: dict[str, str]


def _now_stamp() -> str:
    return _dt.datetime.now().strftime("%Y%m%d-%H%M%S-%f")


def _eprint(message: str) -> None:
    print(message, file=sys.stderr)


def _mask_api_key(api_key: str) -> str:
    api_key = api_key.strip()
    if not api_key:
        return ""
    if len(api_key) <= 10:
        return "*" * len(api_key)
    return f"{api_key[:3]}***{api_key[-4:]}"


def _is_tty() -> bool:
    try:
        return sys.stdin.isatty() and sys.stdout.isatty()
    except Exception:
        return False


def _normalize_base_url(url: str) -> str:
    url = url.strip()
    if not url:
        return url
    return url.rstrip("/") + "/"


def _models_url_candidates(provider_id: str, base_url: str) -> list[str]:
    base = _normalize_base_url(base_url)
    if not base:
        return []

    candidates = [base + "models"]

    if provider_id == "RCode_Google":
        if "/v1beta/" in base:
            candidates.append(base.replace("/v1beta/", "/v1/") + "models")
        elif "/v1/" in base:
            candidates.append(base.replace("/v1/", "/v1beta/") + "models")

    out: list[str] = []
    seen: set[str] = set()
    for url in candidates:
        if url not in seen:
            out.append(url)
            seen.add(url)
    return out


def _download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "rc-opencode-setup/1.0 (+https://docs.right.codes/)",
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=60) as resp, open(dest, "wb") as f:
        shutil.copyfileobj(resp, f)


def _safe_extract_zip(zip_path: Path, dest_dir: Path) -> None:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_root = dest_dir.resolve()
    with zipfile.ZipFile(zip_path) as zf:
        for info in zf.infolist():
            name = info.filename.replace("\\", "/")
            if name.startswith("/"):
                raise ValueError(f"zip 内包含非法路径（绝对路径）：{info.filename}")
            target = (dest_dir / name).resolve()
            if dest_root not in target.parents and target != dest_root:
                raise ValueError(f"zip 内包含非法路径（目录穿越）：{info.filename}")
        zf.extractall(dest_dir)


def _strip_jsonc(text: str) -> str:
    result: list[str] = []
    i = 0
    in_string = False
    escape = False
    while i < len(text):
        ch = text[i]
        if in_string:
            result.append(ch)
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            i += 1
            continue

        if ch == '"':
            in_string = True
            result.append(ch)
            i += 1
            continue

        if ch == "/" and i + 1 < len(text):
            nxt = text[i + 1]
            if nxt == "/":
                i += 2
                while i < len(text) and text[i] not in ("\n", "\r"):
                    i += 1
                continue
            if nxt == "*":
                i += 2
                while i + 1 < len(text) and not (text[i] == "*" and text[i + 1] == "/"):
                    i += 1
                i += 2
                continue

        result.append(ch)
        i += 1
    return "".join(result)


def _remove_trailing_commas(text: str) -> str:
    while True:
        new_text = re.sub(r",(\s*[}\]])", r"\1", text)
        if new_text == text:
            return text
        text = new_text


def _load_json_or_jsonc(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    try:
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError("配置文件不是 JSON 对象")
        return data
    except json.JSONDecodeError:
        cleaned = _remove_trailing_commas(_strip_jsonc(raw))
        data = json.loads(cleaned)
        if not isinstance(data, dict):
            raise ValueError("配置文件不是 JSON 对象")
        return data


def _write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _backup_path(path: Path) -> Path:
    stamp = _now_stamp()
    for _ in range(20):
        suffix = secrets.token_hex(3)
        candidate = path.with_name(f"{path.name}.bak.{stamp}.{suffix}")
        if not candidate.exists():
            return candidate
    i = 0
    while True:
        candidate = path.with_name(f"{path.name}.bak.{stamp}.{i}")
        if not candidate.exists():
            return candidate
        i += 1


def _backup_if_exists(path: Path) -> None:
    if not path.exists():
        return
    backup = _backup_path(path)
    if path.is_dir():
        shutil.copytree(path, backup)
    else:
        shutil.copy2(path, backup)


def _ensure_opencode_installed() -> None:
    if shutil.which("opencode"):
        return
    _eprint("未检测到 `opencode` 命令。请先安装并运行一次 OpenCode：")
    _eprint("")
    _eprint("  npm i -g opencode-ai")
    _eprint("  opencode")
    _eprint("")
    _eprint("然后再重新运行本脚本。")
    raise SystemExit(2)


def _fetch_json(url: str, headers: dict[str, str], timeout: int = 60) -> Any:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "rc-opencode-setup/1.0 (+https://docs.right.codes/)",
            **headers,
        },
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read()
    return json.loads(body.decode("utf-8", errors="replace"))


def _parse_models_response(payload: Any) -> dict[str, dict[str, Any]]:
    items: list[Any] = []
    if isinstance(payload, dict):
        if isinstance(payload.get("data"), list):
            items = payload["data"]
        elif isinstance(payload.get("models"), list):
            items = payload["models"]
        else:
            for v in payload.values():
                if isinstance(v, list) and v and isinstance(v[0], dict):
                    if any(k in v[0] for k in ("id", "name", "model")):
                        items = v
                        break
    elif isinstance(payload, list):
        items = payload

    out: dict[str, dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict):
            continue
        model_id = item.get("id") or item.get("model") or item.get("name")
        if not isinstance(model_id, str) or not model_id.strip():
            continue
        model_id = model_id.strip()
        if model_id.startswith("models/"):
            model_id = model_id.split("/", 1)[1]
        out[model_id] = item
    return out


def _filter_openai_reasoning_variants(models: Iterable[str]) -> list[str]:
    models_list = sorted(set(m.strip() for m in models if m and m.strip()))
    model_set = set(models_list)
    filtered: list[str] = []
    for mid in models_list:
        base, sep, suffix = mid.rpartition("-")
        if sep and suffix in {"low", "medium", "high", "xhigh"}:
            if base in model_set:
                continue
        filtered.append(mid)
    return filtered


def _deep_update_if_key_exists(obj: Any, key_candidates: list[str], value: Any) -> bool:
    if not isinstance(obj, dict):
        return False
    for key in list(obj.keys()):
        for cand in key_candidates:
            if key.lower() == cand.lower():
                obj[key] = value
                return True
    return False


def _apply_numeric_metadata(model_config: dict[str, Any], raw: dict[str, Any]) -> None:
    # 只在模板已经存在对应字段时才覆盖，避免写入 opencode 不认识的键。
    context_window = raw.get("contextWindow") or raw.get("context_window") or raw.get("context_window_size")
    max_output = raw.get("maxOutputTokens") or raw.get("max_output_tokens") or raw.get("max_tokens")

    if context_window is not None:
        _deep_update_if_key_exists(
            model_config,
            ["contextWindow", "context_window", "context_window_size", "contextwindows"],
            context_window,
        ) or _deep_update_if_key_exists(
            model_config.get("options"),
            ["contextWindow", "context_window", "context_window_size", "contextwindows"],
            context_window,
        )

    if max_output is not None:
        _deep_update_if_key_exists(
            model_config,
            ["maxOutputTokens", "max_output_tokens", "max_tokens", "maxoutputtokens"],
            max_output,
        ) or _deep_update_if_key_exists(
            model_config.get("options"),
            ["maxOutputTokens", "max_output_tokens", "max_tokens", "maxoutputtokens"],
            max_output,
        )


def _provider_dict(config: dict[str, Any]) -> dict[str, Any]:
    providers = config.get("provider")
    if isinstance(providers, dict):
        return providers
    providers = config.get("providers")
    if isinstance(providers, dict):
        return providers
    config["provider"] = {}
    return config["provider"]


def _resolve_provider_id(providers: dict[str, Any], preferred: str, expected_base_url: str) -> str | None:
    if preferred in providers:
        return preferred
    expected = _normalize_base_url(expected_base_url)
    for pid, pconf in providers.items():
        if not isinstance(pconf, dict):
            continue
        opts = pconf.get("options")
        if not isinstance(opts, dict):
            continue
        base = opts.get("baseURL") or opts.get("baseUrl") or opts.get("base_url")
        if isinstance(base, str) and _normalize_base_url(base) == expected:
            return pid
    return None


def _get_provider_base_url(provider_conf: dict[str, Any]) -> str | None:
    opts = provider_conf.get("options")
    if not isinstance(opts, dict):
        return None
    for key in ("baseURL", "baseUrl", "base_url"):
        val = opts.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
    return None


def _set_provider_options(
    provider_conf: dict[str, Any],
    api_key: str,
    recommended_base_url: str,
    overwrite_base_url: bool,
) -> None:
    opts = provider_conf.get("options")
    if not isinstance(opts, dict):
        opts = {}
        provider_conf["options"] = opts
    if overwrite_base_url:
        opts["baseURL"] = recommended_base_url.rstrip("/")
    else:
        existing_base_url = opts.get("baseURL") or opts.get("baseUrl") or opts.get("base_url")
        if not isinstance(existing_base_url, str) or not existing_base_url.strip():
            opts["baseURL"] = recommended_base_url.rstrip("/")
    opts["apiKey"] = api_key


def _prompt_api_key(arg_value: str | None) -> str:
    if arg_value and arg_value.strip():
        return arg_value.strip()
    env_value = os.environ.get("RCODE_API_KEY", "").strip()
    if env_value:
        return env_value

    import getpass

    try:
        return getpass.getpass("请输入 Right Code API Key（输入时不回显）：").strip()
    except (KeyboardInterrupt, EOFError):
        _eprint("\n已取消。")
        raise SystemExit(130)


def _render_menu(
    title: str,
    items: list[str],
    selected: set[str],
    cursor: int,
    scroll_top: int,
    view_height: int,
) -> None:
    sys.stdout.write("\x1b[2J\x1b[H")  # clear + home
    sys.stdout.write("\x1b[?25l")  # hide cursor
    print(title)
    print("↑/↓ 移动  Space 勾选  Enter 确认  a 全选  n 全不选  q 退出")
    print("")

    end = min(len(items), scroll_top + view_height)
    if scroll_top > 0:
        print("...（上方还有更多）")
    for idx in range(scroll_top, end):
        mid = items[idx]
        mark = "[x]" if mid in selected else "[ ]"
        pointer = ">" if idx == cursor else " "
        print(f"{pointer} {mark} {mid}")
    if end < len(items):
        print("...（下方还有更多）")

    print("")
    print(f"已选：{len(selected)} / {len(items)}")
    sys.stdout.flush()


def _choose_models_interactive(title: str, items: list[str], selected: set[str]) -> list[str] | None:
    if not items:
        return []

    cursor = 0
    term_lines = shutil.get_terminal_size((80, 24)).lines
    view_height = max(6, term_lines - 8)
    scroll_top = 0

    def clamp_scroll() -> None:
        nonlocal scroll_top
        if cursor < scroll_top:
            scroll_top = cursor
        elif cursor >= scroll_top + view_height:
            scroll_top = cursor - view_height + 1

    try:
        while True:
            clamp_scroll()
            _render_menu(title, items, selected, cursor, scroll_top, view_height)
            key = _read_key()
            if key == "UP":
                cursor = (cursor - 1) % len(items)
            elif key == "DOWN":
                cursor = (cursor + 1) % len(items)
            elif key == "SPACE":
                mid = items[cursor]
                if mid in selected:
                    selected.remove(mid)
                else:
                    selected.add(mid)
            elif key == "A":
                selected = set(items)
            elif key == "N":
                selected = set()
            elif key in ("ENTER",):
                return [m for m in items if m in selected]
            elif key in ("Q", "ESC"):
                return None
    finally:
        sys.stdout.write("\x1b[?25h")  # show cursor
        sys.stdout.write("\x1b[0m")
        sys.stdout.flush()


def _choose_models_fallback(title: str, items: list[str], selected: set[str]) -> list[str] | None:
    print(title)
    print("（当前环境非交互式 TTY，将使用输入序号的方式选择）")
    for idx, mid in enumerate(items, start=1):
        mark = "x" if mid in selected else " "
        print(f"{idx:>3}. [{mark}] {mid}")
    print("")
    raw = input("输入要启用的序号（逗号分隔），直接回车表示保持当前：").strip()
    if not raw:
        return [m for m in items if m in selected]
    if raw.lower() in ("q", "quit", "exit"):
        return None
    chosen: set[int] = set()
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            chosen.add(int(part))
        except ValueError:
            pass
    out: list[str] = []
    for i in sorted(chosen):
        if 1 <= i <= len(items):
            out.append(items[i - 1])
    return out


def _read_key() -> str | None:
    if os.name == "nt":
        import msvcrt

        ch = msvcrt.getwch()
        if ch in ("\x00", "\xe0"):
            ch2 = msvcrt.getwch()
            if ch2 == "H":
                return "UP"
            if ch2 == "P":
                return "DOWN"
            return None
        if ch in ("\r", "\n"):
            return "ENTER"
        if ch == " ":
            return "SPACE"
        if ch in ("a", "A"):
            return "A"
        if ch in ("n", "N"):
            return "N"
        if ch in ("q", "Q"):
            return "Q"
        if ch == "\x1b":
            return "ESC"
        return None

    import termios
    import tty

    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
        if ch == "\x1b":
            nxt = sys.stdin.read(1)
            if nxt == "[":
                nxt2 = sys.stdin.read(1)
                if nxt2 == "A":
                    return "UP"
                if nxt2 == "B":
                    return "DOWN"
            return "ESC"
        if ch in ("\r", "\n"):
            return "ENTER"
        if ch == " ":
            return "SPACE"
        if ch in ("a", "A"):
            return "A"
        if ch in ("n", "N"):
            return "N"
        if ch in ("q", "Q"):
            return "Q"
        return None
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def _choose_models(title: str, items: list[str], selected: set[str]) -> list[str] | None:
    if _is_tty():
        return _choose_models_interactive(title, items, set(selected))
    return _choose_models_fallback(title, items, set(selected))


def _download_template(config_dir: Path, template_url: str, yes: bool) -> None:
    config_dir.mkdir(parents=True, exist_ok=True)

    opencode_json = config_dir / "opencode.json"
    plugins_dir = config_dir / "plugins"

    if (opencode_json.exists() or plugins_dir.exists()) and not yes:
        print(f"即将下载并解压模板到：{config_dir}")
        print("这可能会覆盖你已有的 `opencode.json` / `plugins/`。脚本会先做备份（.bak.*）。")
        ans = input("是否继续？(y/N): ").strip().lower()
        if ans not in ("y", "yes"):
            raise SystemExit(0)

    _backup_if_exists(opencode_json)
    _backup_if_exists(plugins_dir)

    with tempfile.TemporaryDirectory(prefix="rc-opencode-") as td:
        zip_path = Path(td) / "QuickConfiguration.zip"
        print(f"下载模板：{template_url}")
        _download(template_url, zip_path)
        print("解压模板...")
        _safe_extract_zip(zip_path, config_dir)


def _pick_config_path(config_dir: Path) -> Path:
    for name in ("opencode.json", "opencode.jsonc"):
        p = config_dir / name
        if p.exists():
            return p
    return config_dir / "opencode.json"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Right Code × OpenCode 一键配置（下载模板、写入 API Key、拉取模型并勾选写入 opencode.json）"
    )
    parser.add_argument("--config-dir", help="OpenCode 配置目录（默认：~/.config/opencode）")
    parser.add_argument("--template-url", default=TEMPLATE_ZIP_URL, help="模板 zip 地址")
    parser.add_argument("--skip-template", action="store_true", help="跳过模板下载/解压，仅更新现有配置")
    parser.add_argument(
        "--overwrite-base-url",
        action="store_true",
        help="覆盖 provider.options.baseURL（默认不覆盖，保留模板/用户现有渠道）",
    )
    parser.add_argument("--api-key", help="Right Code API Key（不传则交互输入；也可用环境变量 RCODE_API_KEY）")
    parser.add_argument("--print-api-key", action="store_true", help="输出完整 API Key（默认仅掩码）")
    parser.add_argument("--yes", action="store_true", help="跳过确认提示")
    args = parser.parse_args()

    _ensure_opencode_installed()

    config_dir = Path(args.config_dir).expanduser() if args.config_dir else Path.home() / ".config" / "opencode"
    config_dir = config_dir.expanduser()

    api_key = _prompt_api_key(args.api_key)
    if not api_key:
        _eprint("API Key 为空，已退出。")
        return 2

    print("")
    print("========== 配置概览 ==========")
    print(f"配置目录：{config_dir}")
    if args.print_api_key:
        print(f"API Key：{api_key}")
    else:
        print(f"API Key：{_mask_api_key(api_key)}（可用 --print-api-key 输出完整）")
    print("=============================")
    print("")

    if not args.skip_template:
        _download_template(config_dir, args.template_url, yes=args.yes)

    config_path = _pick_config_path(config_dir)
    if not config_path.exists():
        _eprint(f"未找到配置文件：{config_path}")
        _eprint("请确认模板已正确解压，或手动创建 opencode.json 后重试。")
        return 2

    config = _load_json_or_jsonc(config_path)
    providers = _provider_dict(config)

    specs: list[ProviderSpec] = [
        ProviderSpec(
            provider_id="RCode_ClaudeCode",
            label="Claude",
            recommended_base_url="https://right.codes/claude-aws/v1",
            headers={"x-api-key": api_key, "Authorization": f"Bearer {api_key}"},
        ),
        ProviderSpec(
            provider_id="RCode_OpenAI",
            label="GPT / Codex",
            recommended_base_url="https://right.codes/codex/v1",
            headers={"Authorization": f"Bearer {api_key}", "x-api-key": api_key},
        ),
        ProviderSpec(
            provider_id="RCode_Google",
            label="Gemini",
            recommended_base_url="https://right.codes/gemini/v1",
            headers={"x-goog-api-key": api_key, "Authorization": f"Bearer {api_key}"},
        ),
    ]

    # 拉取模型列表
    remote_models: dict[str, dict[str, dict[str, Any]]] = {}
    print("拉取模型列表...")
    for spec in specs:
        pid = _resolve_provider_id(providers, spec.provider_id, spec.recommended_base_url) or spec.provider_id
        provider_conf = providers.get(pid)

        effective_base_url = spec.recommended_base_url
        if isinstance(provider_conf, dict):
            configured_base_url = _get_provider_base_url(provider_conf)
            if configured_base_url:
                effective_base_url = configured_base_url

        models_urls = _models_url_candidates(spec.provider_id, effective_base_url)
        parsed: dict[str, dict[str, Any]] = {}
        last_error: str | None = None
        last_url: str | None = None
        for models_url in models_urls:
            last_url = models_url
            try:
                payload = _fetch_json(models_url, spec.headers)
                parsed = _parse_models_response(payload)
                last_error = None
                break
            except urllib.error.HTTPError as e:
                last_error = f"HTTP {e.code}"
            except urllib.error.URLError as e:
                last_error = f"网络错误：{e}"
            except Exception as e:
                last_error = str(e)

        if spec.provider_id == "RCode_OpenAI":
            keep = _filter_openai_reasoning_variants(parsed.keys())
            parsed = {k: parsed[k] for k in keep if k in parsed}

        remote_models[spec.provider_id] = parsed
        if parsed:
            print(f"- {spec.label}: {len(parsed)} 个模型")
        else:
            if last_error and last_url:
                _eprint(f"- {spec.label}: 拉取失败（{last_error}）{last_url}")
            else:
                _eprint(f"- {spec.label}: 未获取到模型列表（将仅使用模板内置模型）")
    print("")

    # 更新 provider options + models（按现有模板结构保留参数）
    for spec in specs:
        pid = _resolve_provider_id(providers, spec.provider_id, spec.recommended_base_url)
        if not pid:
            _eprint(f"未在 opencode.json 中找到 provider：{spec.provider_id}")
            _eprint("请确认你使用的是 Right Code 提供的 QuickConfiguration 模板。")
            return 2

        provider_conf = providers.get(pid)
        if not isinstance(provider_conf, dict):
            _eprint(f"provider `{pid}` 的配置不是对象，已跳过。")
            continue

        _set_provider_options(
            provider_conf,
            api_key,
            spec.recommended_base_url,
            overwrite_base_url=bool(args.overwrite_base_url),
        )

        existing_models = provider_conf.get("models")
        if not isinstance(existing_models, dict):
            existing_models = {}
        existing_ids = sorted(k for k in existing_models.keys() if isinstance(k, str))

        remote = remote_models.get(spec.provider_id, {})
        candidate_ids = sorted(set(existing_ids) | set(remote.keys()))
        if spec.provider_id == "RCode_OpenAI":
            candidate_ids = _filter_openai_reasoning_variants(candidate_ids)

        if not candidate_ids:
            print(f"{spec.label}: 未获取到模型列表，跳过模型选择（仅写入 API Key / baseURL）。")
            continue

        preselect = set(existing_ids)
        chosen = _choose_models(f"选择要启用的 {spec.label} 模型", candidate_ids, preselect)
        if chosen is None:
            _eprint("已取消。")
            return 130

        template_model: dict[str, Any] | None = None
        for mid in existing_ids:
            conf = existing_models.get(mid)
            if isinstance(conf, dict):
                template_model = conf
                break

        new_models: dict[str, Any] = {}
        for mid in chosen:
            if mid in existing_models and isinstance(existing_models[mid], dict):
                new_models[mid] = existing_models[mid]
                continue
            if template_model is not None:
                new_conf = copy.deepcopy(template_model)
            else:
                new_conf = {}
            raw = remote.get(mid) or {}
            if isinstance(new_conf, dict) and isinstance(raw, dict):
                _apply_numeric_metadata(new_conf, raw)
            new_models[mid] = new_conf

        provider_conf["models"] = new_models
        print(f"{spec.label}: 已写入 {len(new_models)} 个模型到 provider `{pid}`")
        print("")

    _backup_if_exists(config_path)
    _write_json(config_path, config)

    print("✅ 已完成配置写入：")
    print(f"- {config_path}")
    print("")
    print("下一步：运行 `opencode`，并在 TUI 中输入 `/models` 验证模型列表。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
