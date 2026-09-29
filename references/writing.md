# Writing for the ear

The primary script is edited for listening — not a stitched-together summary of web pages. Depth follows audience and purpose: adult experts get adult depth; never hard-code child-simplification.

## Structure

- An `#` title, then a short opening that tells the listener what this brief covers and why it is worth their next few minutes.
- One `##` section per item, in plan order, with context and transitions a listener can follow without scrolling back.
- Within an item: facts first, then `why_it_matters`, then whatever explanation the planned concepts need.
- A short closing; for child audiences, optionally one open question.

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

The script body is the deliverable; keep it directly speakable. It must contain none of:

- source URLs
- citation markers or footnote calls
- Markdown tables
- images
- editor notes, stage directions, or review annotations

Use only: `#` title, `##` per item, plain paragraphs. Skip emphasis decoration a TTS voice would read awkwardly. Provenance and editing notes live in `sources.json`, `facts.json`, and `manifest.json` — never in the script.

## Children {#children}

Only when `audience.is_child` is true:

- Judge age-appropriateness from the stated age; avoid gratuitous gore, violence, or adult detail — but major events are not automatically banned. The test is whether the child is better off knowing.
- No fear-making, no sensational framing, no doom delivery.
- Never bend facts to be child-friendly; adjust the explanation, not the truth.
- Prefer items that open onto science, the world, nature, or how society works.
- The closing open question, when used, invites choice, imagination, reasoning, or explaining why — never a knowledge quiz with one right answer.
