---
title: Codex 相关疑问
icon: hugeicons:chat-gpt
order: 1
footer: false
---

## 如何在Codex中使用最新模型

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