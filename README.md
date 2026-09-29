# Briefcast

English · [简体中文](README.zh-CN.md)

Turn any topic into a listener-ready brief. Your AI agent researches live sources, verifies what matters, selects what is worth the audience's time, and writes a script meant to be heard — with an optional second-language version written independently at a controlled difficulty.

Briefcast's product is text. It does not generate audio or video, publish, or schedule; whatever narrates or distributes the brief consumes the Markdown exactly as produced. Any TTS engine, human narrator, or downstream pipeline can read `brief.primary.md` straight through.

## Install

Using [vercel-labs/skills](https://github.com/vercel-labs/skills):

```sh
npx skills add LcpMarvel/briefcast
```

To target Codex and Claude Code in the current project:

```sh
npx skills add LcpMarvel/briefcast --skill briefcast --agent codex claude-code
```

Add `--global` for a user-level installation. The installer requires Node.js/npm. The skill itself is pure instructions for your agent and needs no runtime beyond the agent's own web research tools.

## Try it

Ask your agent, in any language:

> 给一个二年级孩子做一期今天值得知道的世界新闻，中文，加一版约 600L 的英文。

> 把过去 24 小时 AI Agent 领域最重要的新闻，写成约 8 分钟的播报稿。

> Brief our investors on this week's gene-testing industry news — about six minutes, English.

> 根据这几个 URL，写一期适合播客口播的 10 分钟总结：…

The agent normalizes the request into a run profile and asks only what genuinely changes the result — audience, language, difficulty, length. Everything else it infers.

## How it works

PROFILE → RESEARCH → VERIFY → SELECT → PLAN → WRITE → ADAPT → REVIEW → PACKAGE

| Stage | What the agent does |
| --- | --- |
| Research & verify | live web research for anything current; source priority and cross-checking; every fact carries provenance and confidence |
| Select | editorial judgment on relevance, importance, novelty, explainability, diversity, audience fit — the requested item count is a target, not a quota |
| Plan | a language-neutral content plan (core facts, why it matters, terms to explain, must-not-overstate) shared by every language version |
| Write | the primary script is edited for the ear: spoken register, terms explained on first use, numbers in perceptible scales, no citation clutter |
| Adapt | the second-language version is composed independently from the same plan — never a translation — to a requested difficulty (Lexile, CEFR, or plain words), then gets its own listening review |

A difficulty request such as "600L 左右" is a generation target (aim 550–650), not a certified measurement; the skill never claims official Lexile certification.

## What you get

Each run creates a directory in your working folder:

```text
briefcast-runs/20260929-0715-world-news/
  brief.yaml            # normalized profile: topic, audience, languages, difficulty
  sources.json          # every candidate source with metadata and verification status
  facts.json            # verified statements with provenance
  content-plan.json     # the shared editorial plan
  brief.primary.md      # the brief — clean Markdown, ready to read aloud
  brief.secondary.md    # optional second-language version
  manifest.json         # status, artifacts, warnings
```

Downstream stages read `manifest.json` alone to find everything. An interrupted run keeps its artifacts; re-invoking resumes from the first incomplete stage without repeating research. If the second language fails, the primary brief still ships, marked `partial`.

## Compose

Briefcast stops at text on purpose:

```text
briefcast → TEXT → any narrator / TTS engine / video pipeline
```

The scripts contain only `#`/`##` headings and plain paragraphs — no URLs, citation markers, tables, or images — so engines read them straight through. For expressive Gemini speech, [gemini-tts-director](https://github.com/LcpMarvel/gemini-tts-director) consumes these scripts as written.

## Documentation

- [Skill entry point](SKILL.md) — instructions for the editing agent.
- [Research and verification](references/research.md) — when live research is mandatory, source records, cross-checking.
- [Selection and planning](references/planning.md) — editorial criteria and the shared content plan.
- [Writing for the ear](references/writing.md) — spoken-register rules, the clean-text contract, child audiences.
- [Secondary language](references/secondary-language.md) — sibling-not-translation, difficulty control, the review pass.
- [Output contract](references/output-contract.md) — run directory, manifest schema, resumable runs.

Repository instructions are in English; briefs and user-facing material follow the requested language.
