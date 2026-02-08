---
title: Codex 相关疑问
icon: hugeicons:chat-gpt
order: 1
footer: false
---

## 如何在Codex中使用最新模型

:::tip 通用启用方式（推荐）
- 打开 `config.toml`，找到这一行：`model = "gpt-5.2"`。
- 把它改成你想启用的模型（例如：`model = "gpt-5.3-codex"`），然后保存。
- 保存后重启你正在用的客户端即可生效：`Codex CLI` / `Codex App` / `VSCode` 插件。
- **重要：启用后不要在会话里切换模型。** 如果切换过，请重新执行：`codex -m gpt-5.3-codex -c model_reasoning_effort="xhigh"`。
:::

### CLI 使用方法

1. 打开终端，使用下面命令启动 Codex：

```bash
codex -m gpt-5.3-codex -c model_reasoning_effort="xhigh"
```

2. 进入对话后，直接提问即可使用最新模型。

::: tip
如果你当前已经打开了 `codex`，先按 `Ctrl + C` 退出，再用上面的命令重新启动。
:::

### VSCode 版本使用方法

:::warning 版本提示
插件教程仅适用于当前支持的 Codex 插件版本 `v0.5.72`。
:::

1. 首先打开你的Vscode，查看你的VScode插件版本号
::: important
**这里一定要把插件换成预发布版本**
:::

![](/assets/image/rc_questions/rc-01.webp)

2. 找到Vscode的插件目录
> 首先打开你的`终端`程序，不管你是Windows还是MacOS系统
> 然后根据系统，运行下面的命令，打开vscode的插件目录
:::tabs
@tab Windows
CMD命令行：
```bash
start "" "%userprofile%\.vscode\extensions"
```

@tab MacOS
```bash
open "$HOME/.vscode/extensions"
```
:::

3. 在目录下寻找文件开头为 `openai.chatgpt`  的目录，可能会有多个，需要对应你查看的插件的版本号
::: tip
**比如上图显示的版本号为 `0.5.72` ，则你需要找的文件夹开头应该是：**

`openai.chatgpt-0.5.72-`
:::

4. 打开文件夹，接着进入 `webview\assets` 目录，这个目录会有一大堆的js文件

![](/assets/image/rc_questions/rc-02.webp)

5. 下载如下的压缩包，解压后拿到js文件，将这个js文件复制到 `webview\assets` 目录，替换原有js文件

<CodexDownload version="0.5.72" summary="已适配最新的 GPT-5.3-Codex 模型" />

6. 重启Vscode，观察模型列表是否有了最新的模型

<script setup>
import CodexDownload from "@source/.vuepress/components/CodexDownload.vue";
</script>
