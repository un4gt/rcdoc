<template>
  <div class="codex-download">
    <div class="codex-download__header">
      <span class="codex-download__tag">
        <svg class="codex-download__tag-icon" viewBox="0 0 16 16" fill="currentColor">
          <path d="M2.5 1A1.5 1.5 0 0 0 1 2.5v4.586a1.5 1.5 0 0 0 .44 1.06l5.953 5.954a1.5 1.5 0 0 0 2.121 0l4.586-4.586a1.5 1.5 0 0 0 0-2.121L8.146 1.44A1.5 1.5 0 0 0 7.086 1H2.5zM5 4.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
        </svg>
        当前支持的Codex插件版本 v{{ version }}
      </span>
    </div>
    <div class="codex-download__summary">
      <svg class="codex-download__summary-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"
        stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10" />
        <line x1="12" y1="16" x2="12" y2="12" />
        <line x1="12" y1="8" x2="12.01" y2="8" />
      </svg>
      <span class="codex-download__summary-text">{{ summary }}</span>
    </div>
    <div class="codex-download__file-card">
      <div class="codex-download__file-info">
        <svg class="codex-download__file-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"
          stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
          <polyline points="7 10 12 15 17 10" />
          <line x1="12" y1="15" x2="12" y2="3" />
        </svg>
        <div class="codex-download__file-meta">
          <span class="codex-download__file-name">{{ fileName }}</span>
          <span class="codex-download__file-size">ZIP 压缩包</span>
        </div>
      </div>
      <a class="codex-download__btn" :href="downloadUrl" download>
        <svg class="codex-download__btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"
          stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
          <polyline points="7 10 12 15 17 10" />
          <line x1="12" y1="15" x2="12" y2="3" />
        </svg>
        立即下载
      </a>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  version: { type: String, default: '0.5.72' },
  summary: { type: String, default: '下载以下替换文件，解压后将 JS 文件复制到 webview\\assets 目录中覆盖原文件，重启 VSCode 即可使用最新模型。' },
  fileName: { type: String, default: 'vscode-codex-replace.zip' },
  downloadUrl: { type: String, default: '/assets/file/codex/vscode-codex-replace.zip' },
})
</script>

<style>
.codex-download {
  margin: 1.2em 0;
  border-radius: 12px;
  border: 1px solid var(--rc-brand-tint, rgba(224, 107, 49, 0.18));
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.9) 0%, rgba(255, 247, 242, 0.9) 100%);
  padding: 1.25rem 1.5rem;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  transition: border-color 0.3s, box-shadow 0.3s;
}
.codex-download:hover {
  border-color: rgba(224, 107, 49, 0.35);
  box-shadow: 0 8px 24px rgba(224, 107, 49, 0.1);
}
.codex-download__header {
  margin-bottom: 0.75rem;
}
.codex-download__tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--rc-brand, #e06b31);
  background: var(--rc-brand-tint, rgba(224, 107, 49, 0.18));
  line-height: 1.6;
}
.codex-download__tag-icon {
  width: 14px;
  height: 14px;
  flex-shrink: 0;
}
.codex-download__summary {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin: 0 0 1rem;
  padding: 10px 14px;
  border-radius: 8px;
  border-left: 3px solid var(--rc-brand, #e06b31);
  background: rgba(224, 107, 49, 0.06);
  transition: background 0.2s;
}
.codex-download__summary-icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
  margin-top: 2px;
  color: var(--rc-brand, #e06b31);
  opacity: 0.8;
}
.codex-download__summary-text {
  font-size: 0.9rem;
  color: var(--text-color, #374151);
  line-height: 1.65;
}
.codex-download__file-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 0.85rem 1rem;
  border-radius: 10px;
  border: 1px solid rgba(224, 107, 49, 0.12);
  background: rgba(255, 255, 255, 0.6);
  transition: border-color 0.2s;
}
.codex-download__file-card:hover {
  border-color: rgba(224, 107, 49, 0.28);
}
.codex-download__file-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  min-width: 0;
}
.codex-download__file-icon {
  width: 28px;
  height: 28px;
  flex-shrink: 0;
  color: var(--rc-brand, #e06b31);
}
.codex-download__file-meta {
  display: flex;
  flex-direction: column;
  min-width: 0;
}
.codex-download__file-name {
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--text-color, #1f2937);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.codex-download__file-size {
  font-size: 0.78rem;
  color: var(--text-color-lighter, #9ca3af);
  margin-top: 1px;
}
.codex-download__btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 18px;
  border-radius: 8px;
  font-size: 0.88rem;
  font-weight: 600;
  color: #fff;
  background: var(--rc-brand, #e06b31);
  text-decoration: none;
  white-space: nowrap;
  transition: background 0.2s, box-shadow 0.2s, transform 0.15s;
  box-shadow: 0 2px 8px rgba(224, 107, 49, 0.25);
}
.codex-download__btn:hover {
  background: var(--rc-brand-dark, #c85b28);
  box-shadow: 0 4px 14px rgba(224, 107, 49, 0.35);
  transform: translateY(-1px);
  color: #fff;
  text-decoration: none;
}
.codex-download__btn:active {
  transform: translateY(0);
}
.codex-download__btn-icon {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}

/* Dark mode */
html[data-theme="dark"] .codex-download {
  background: linear-gradient(135deg, rgba(30, 30, 35, 0.9) 0%, rgba(34, 26, 22, 0.9) 100%);
  border-color: rgba(224, 107, 49, 0.22);
}
html[data-theme="dark"] .codex-download:hover {
  border-color: rgba(224, 107, 49, 0.42);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}
html[data-theme="dark"] .codex-download__file-card {
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(224, 107, 49, 0.15);
}
html[data-theme="dark"] .codex-download__file-card:hover {
  border-color: rgba(224, 107, 49, 0.32);
}
html[data-theme="dark"] .codex-download__summary code {
  background: rgba(224, 107, 49, 0.2);
  color: var(--rc-brand-light, #f07a3f);
}
html[data-theme="dark"] .codex-download__summary {
  background: rgba(224, 107, 49, 0.08);
}
html[data-theme="dark"] .codex-download__summary-text {
  color: rgba(255, 255, 255, 0.85);
}
html[data-theme="dark"] .codex-download__file-name {
  color: rgba(255, 255, 255, 0.9);
}
html[data-theme="dark"] .codex-download__file-size {
  color: rgba(255, 255, 255, 0.45);
}
html[data-theme="dark"] .codex-download__btn {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}
html[data-theme="dark"] .codex-download__btn:hover {
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
}

/* Responsive */
@media (max-width: 540px) {
  .codex-download__file-card {
    flex-direction: column;
    align-items: stretch;
  }
  .codex-download__btn {
    justify-content: center;
  }
}
</style>
