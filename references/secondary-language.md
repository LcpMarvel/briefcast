# Secondary language version

The secondary script is a sibling of the primary, not its translation. Both are composed from the same base:

```text
verified facts + content plan
   ├── primary-language brief
   └── secondary-language brief
```

The forbidden default is `primary script → translate → secondary script`. The two versions share the factual core and may differ in length, order, narrative approach, and explanations. The secondary must read as originally written in its own language, with its own natural idiom — no sentence shapes or calques carried over from the primary. If you notice yourself tracking the primary's phrasing, stop and restart from the plan.

## Difficulty control

Difficulty arrives as Lexile ("600L 左右"), CEFR ("B1"), or natural language ("简单一点", "小学水平", "normal adult news"). Normalize any of these into concrete constraints before composing:

- sentence length — one main idea per sentence
- vocabulary tier — high-frequency, concrete words; how many new hard words per item
- syntax — short clauses, no deep nesting, no long attributive chains or dense noun phrases
- idiom and register — which idioms, if any, are in bounds

A Lexile target is a generation goal, not a measurement: 600 ± 50 means aim inside 550–650, and the output is never certified at any level — never claim official Lexile certification. Listening-oriented targets (`purpose: listening`) are optimized for what the ear follows on first pass, not for reading-complexity scores:

- Short sentences, one main idea each.
- High-frequency concrete words; cut abstract academic vocabulary the topic does not require.
- Topic-essential terms may exceed the target — explain each in plain words at first use.
- Cap the new hard words an item introduces; deliberate repetition of core words helps the ear, it is not a style flaw.

## Review

After composing, run a separate review pass over the secondary script — not while writing it:

1. Flag overlong sentences → split them.
2. Flag low-frequency words the target does not need → replace or explain.
3. Flag complex nesting → flatten.
4. Check every core term is explained at first use.
5. Re-check facts against `facts.json`: simplification must not have changed meaning, dropped attribution, or shaved a `must_not_overstate` qualifier.

Record the outcome in `manifest.json` under `languages.secondary.review`. If the review cannot pass, keep the draft, mark it, and leave the language below `reviewed` — never present an unreviewed script as finished.
