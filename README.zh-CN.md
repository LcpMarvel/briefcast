# Briefcast

[English](README.md) · 简体中文

把任意主题做成一期"值得听"的简报。你的 AI Agent 会真实检索最新信息、核验事实、挑选值得占用听众时间的内容，然后写成适合口播的稿子；还可以按指定难度独立创作第二语言版本。

Briefcast 的产物是文本。它不生成音频或视频、不发布、不调度；任何 TTS、真人主播或下游流水线都能直接消费产出的 Markdown。

## 安装

使用 [vercel-labs/skills](https://github.com/vercel-labs/skills)：

```sh
npx skills add LcpMarvel/briefcast
```

只安装到当前项目的 Codex 或 Claude Code：

```sh
npx skills add LcpMarvel/briefcast --skill briefcast --agent codex claude-code
```

添加 `--global` 可安装到用户目录。安装 CLI 需要 Node.js/npm；skill 本体是纯指令，除 Agent 自带的检索工具外不需要任何运行时。

## 试一试

用任何语言吩咐你的 Agent：

> 给一个二年级孩子做一期今天值得知道的世界新闻，中文，加一版约 600L 的英文。

> 把过去 24 小时 AI Agent 领域最重要的新闻，写成约 8 分钟的播报稿。

> 给生物科技投资人做一期本周基因检测行业简报，英文，6 分钟左右。

> 根据这几个 URL，写一期适合播客口播的 10 分钟总结：…

Agent 会把请求归一成一份 run profile；只有缺失且会显著改变结果的配置才会询问——听众、语言、难度、长度——其余全部从自然语言推断。

## 工作方式

PROFILE → RESEARCH → VERIFY → SELECT → PLAN → WRITE → ADAPT → REVIEW → PACKAGE

| 阶段 | Agent 做什么 |
| --- | --- |
| 检索与核验 | 涉及最新信息时真实联网检索；来源分级、交叉验证；每条事实带出处和置信度 |
| 筛选 | 按相关性、重要性、新信息量、可讲性、多样性、听众契合度做编辑判断；条数是目标不是配额 |
| 规划 | 先写语言中立的内容计划（核心事实、为什么值得知道、需要解释的概念、不许夸大的点），所有语言版本共用 |
| 写作 | 主语言稿为耳朵重新编辑：口语语域、术语首现即解释、数字换成可感知的尺度、正文零引用噪音 |
| 改编 | 第二语言从同一份计划独立创作——绝不翻译主稿——按指定难度（Lexile、CEFR 或自然语言）生成，并做独立的听力审校 |

难度要求（如"600L 左右"）是生成目标区间（瞄准 550–650），不是官方测量；本 skill 不会声称文本通过 Lexile 认证。

## 产出

每次执行在工作目录创建一个 run 目录：

```text
briefcast-runs/20260929-0715-world-news/
  brief.yaml            # 归一后的 profile：主题、听众、语言、难度
  sources.json          # 全部候选来源及元数据、核验状态
  facts.json            # 带出处的事实陈述
  content-plan.json     # 共用的编辑计划
  brief.primary.md      # 简报正文——干净的 Markdown，可直接朗读
  brief.secondary.md    # 可选的第二语言版本
  manifest.json         # 状态、产物清单、警告
```

下游只需要读 `manifest.json` 就能找到全部产物。中途中断的 run 保留已完成产物，再次调用从第一个未完成阶段续跑，不重复昂贵的检索。第二语言失败时主语言稿照常交付，状态标为 `partial`。

## 组合

Briefcast 有意止步于文本：

```text
briefcast → 文本 → 任意主播 / TTS 引擎 / 视频流水线
```

稿子只含 `#`/`##` 标题和纯段落——没有 URL、引用标记、表格、图片——引擎可以直接顺读。想要有表现力的 Gemini 语音，[gemini-tts-director](https://github.com/LcpMarvel/gemini-tts-director) 可以直接消费这些稿子。

## 文档

- [Skill 入口](SKILL.md)——编辑 Agent 的完整指令。
- [检索与核验](references/research.md)——何时必须联网检索、来源记录、交叉验证。
- [筛选与规划](references/planning.md)——编辑判断标准与共用内容计划。
- [为耳朵写作](references/writing.md)——口语写作规则、干净文本契约、儿童听众。
- [第二语言](references/secondary-language.md)——"是姊妹篇不是翻译"、难度控制、独立审校。
- [输出契约](references/output-contract.md)——run 目录、manifest 结构、可续跑。

仓库说明为英文；简报与面向用户的内容跟随请求的语言。
