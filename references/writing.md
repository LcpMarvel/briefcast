# Writing for the ear

The primary script is edited for listening — not a stitched-together summary of web pages. Depth follows audience and purpose: adult experts get adult depth; never hard-code child-simplification.

## Structure

The script is a continuous monologue, not a document. Every character in the file is meant to be spoken, in order; nothing exists for the eye alone.

- Open with a spoken title line: a sentence that names the brief and what it covers ("你好呀，今天的新闻时间到了……"), doing in speech what a headline does in print.
- One paragraph group per item, in plan order. Structure is carried by spoken transitions ("第一条新闻……", "接下来……"), never by visual separators — a listener who cannot scroll back must always know where they are.
- Within an item: facts first, then `why_it_matters`, then whatever explanation the planned concepts need.
- Close briefly; for child audiences, optionally one open question.

## Ear rules

- Explain a necessary term the first time it appears; do not pre-explain vocabulary this audience obviously owns.
- Convert numbers into perceptible scales when it helps — comparisons to known sizes, costs, everyday quantities — and drop precision the ear cannot hold.
- No visual-dependent phrasing: no "如下图", "as the table shows", "前面第三点说过的". The listener cannot look back.
- Spoken register, plain and direct. No press-release, paper-abstract, or marketing cadence.
- Never fabricate facts, people, quotes, or scene detail. Keep fact, speculation, and opinion distinguishable by wording and attribution ("研究人员认为", "in the company's words").
- Sentences sized for one pass of the ear; paragraphs short enough to breathe.

## Length

Aim the primary script at `target_duration_minutes` using the rates in [Output contract](output-contract.md#duration-estimation). Adjust by choosing fewer or more items, or varying depth per item — not by compressing sentences into density the ear cannot parse.

## Clean text

The script is the deliverable: plain text where every character is meant to be spoken. It must contain none of:

- source URLs
- citation markers or footnote calls
- Markdown syntax of any kind — no `#` headings, no bold/italic markers, no bullet lists, no tables, no images
- editor notes, stage directions, or review annotations

Paragraph breaks are the only formatting: they group thoughts and give a narrator natural pause points, and no engine reads them aloud. A display title for apps and covers belongs in `manifest.json` (`languages.*.title`, one per language), never in the script — in audio, the spoken opening line does the title's job. Provenance and editing notes live in `sources.json`, `facts.json`, and `manifest.json` — never in the script.

## Children {#children}

Only when `audience.is_child` is true:

- Judge age-appropriateness from the stated age; avoid gratuitous gore, violence, or adult detail — but major events are not automatically banned. The test is whether the child is better off knowing.
- No fear-making, no sensational framing, no doom delivery.
- Never bend facts to be child-friendly; adjust the explanation, not the truth.
- Prefer items that open onto science, the world, nature, or how society works.
- The closing open question, when used, invites choice, imagination, reasoning, or explaining why — never a knowledge quiz with one right answer.
