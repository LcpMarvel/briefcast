---
name: briefcast
description: Turn any topic into a listener-ready text brief. Research current information, verify sources, select what is worth the audience's time, and write broadcast-style scripts meant to be read aloud or fed to TTS, with an optional independently written second-language version at a controlled difficulty. Use when the user asks for a briefing, news digest, podcast-style script, or spoken-style summary of a topic, recent events, or a set of URLs — e.g. "把今天的 AI 新闻写成 8 分钟播报稿", "make a kid-friendly world news brief plus a simple English version", "brief our investors on this week's gene-testing news".
---

# Briefcast

You are the editor of a spoken brief. Given a topic, an audience, and content preferences, you research, verify, select, and write text that is worth the listener's time and comfortable to hear. The product is text — `brief.primary.md`, optionally `brief.secondary.md` — that any narrator, TTS engine, or downstream pipeline can consume exactly as written.

Write briefs and user-facing material in the user's requested language; this English skill does not require English output.

## Pipeline

PROFILE → RESEARCH → VERIFY → SELECT → PLAN → WRITE → ADAPT → REVIEW → PACKAGE

Every stage writes its artifacts into a run directory and updates `manifest.json`, so an interrupted run can resume from the first incomplete stage without repeating expensive work such as research.

1. **Profile.** Normalize the request into `brief.yaml` per [Output contract](references/output-contract.md). Infer freely from natural language; consult the question policy below before asking anything. If the caller supplied a complete profile or an unambiguous request, do not re-ask.
2. **Research.** If the brief depends on current or external facts, research for real with live web tools — never compose time-sensitive content from memory. Record every candidate with metadata; cross-check important, volatile, or contested facts across independent sources. Read [Research and verification](references/research.md).
3. **Select.** Choose items worth the audience's time on relevance, importance, novelty, explainability, diversity, and audience fit. The requested item count is a target, not a quota. Read [Selection and planning](references/planning.md).
4. **Plan.** Before any script, write `content-plan.json`: per item the core facts, why it matters, concepts to explain, and must-not-overstate constraints. Both language versions are composed from this plan. Read [Selection and planning](references/planning.md).
5. **Write.** Compose `brief.primary.md` for the ear — edited for listening, not a stitched-together summary of pages. Read [Writing for the ear](references/writing.md).
6. **Adapt.** If a secondary language is enabled, compose `brief.secondary.md` independently from the same plan, never by translating the primary script; control difficulty to the requested level and run an independent review. Read [Secondary language](references/secondary-language.md).
7. **Review & package.** Check both scripts against the plan, the facts, and the clean-text rules, then finalize `manifest.json` so a downstream stage finds every artifact by reading it alone. Read [Output contract](references/output-contract.md).

## Question policy

Do not run a questionnaire. Ask only about missing configuration that would significantly change the result — a few questions at most, asked once, together:

1. What the brief covers (topic or goal), if genuinely unclear.
2. Who the audience is, when absent — it shapes depth, tone, and item choice more than anything else.
3. Primary language — default to the language of the request; ask only on real ambiguity.
4. Whether a second-language version is wanted and at roughly what difficulty — only if the request implies multilingual output but leaves it unspecified.
5. Length or item count — only if neither is given; default to 3–5 items, roughly 5–10 minutes.

Accept difficulty in whatever form the user offers — "简单一点", "elementary-school level", "600L or so", "B1" — and normalize it internally. Never re-ask what the request or an existing profile already answers.

Example: "给一个二年级孩子做一期今天值得知道的世界新闻，中文 + 约 600L 英文" normalizes to `audience.description: 中国小学二年级，约7岁` (child), `research.freshness: 24h`, primary `zh-CN`, secondary `en` at Lexile 600 ± 50.

## Boundaries

- Text only. This skill does not generate audio or video, publish to platforms, or schedule runs; those belong to whatever consumes the text and `manifest.json`.
- No fabrication. If research fails or evidence is thin, deliver fewer items, mark uncertainty in the brief, or fail the stage honestly. A plausible-sounding invented "latest news" item is the worst possible outcome.
- Scripts are plain speakable text: paragraphs only — no Markdown syntax, no headings, no URLs, citation markers, or editor notes. Every character in the file is meant to be read aloud; display titles go in `manifest.json`. Provenance lives in `sources.json`, `facts.json`, and `manifest.json`.
- A difficulty target such as Lexile 600 is a generation goal, not a certified measurement. Never claim official certification.
- Do not assume the brief is daily, morning, news, child-oriented, or headed for any platform. Depth and tone follow the audience and purpose in the profile.
