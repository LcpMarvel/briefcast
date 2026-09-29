# Selection and planning

## Select

The goal is a brief worth the listener's time, not a summary of search results. Judge candidates on:

- **relevance** — actually about the requested topic
- **importance** — worth this audience's time
- **novelty** — new information, not a rehash
- **explainability** — can be told clearly in speech, within the length budget
- **diversity** — items don't repeat one underlying story
- **audience fit** — right subject, depth, and tone for these listeners

`research.item_count` is a target. If only two items are genuinely worth telling, deliver two and record why in `manifest.json` warnings; padding with weak material to hit a count is a defect. Mark each candidate in `sources.json` as used, or with an `exclusion_reason`.

## Plan

Write `content-plan.json` before any script. It is the single editorial source both language versions are composed from, so keep it complete, language-neutral, and free of the primary language's phrasing — whatever the plan asserts is what every version must say:

```json
{
  "brief_angle": "The one-line editorial take for the whole brief.",
  "items": [
    {
      "id": "item-1",
      "working_title": "Reusable launcher completes second flight",
      "core_facts": ["fact-1", "fact-2"],
      "why_it_matters": "Cheaper launches change who can reach orbit.",
      "concepts_to_explain": [
        {"term": "orbital flight", "note": "first-time listeners; each language version explains it its own way"}
      ],
      "must_not_overstate": ["second flight only; not a proven operational system"],
      "source_refs": ["src-1"]
    }
  ],
  "closing": {"open_question": null}
}
```

- `core_facts` reference `facts.json` ids. Nothing enters a script that is not a planned fact; nothing is planned that is not in `facts.json` — add it there first.
- Every item needs a `why_it_matters` that the listener actually receives.
- `must_not_overstate` collects verified-but-inflatable claims (early results, preliminary numbers, single-source reports) that every script must keep in proportion.
- Order items for the ear — strong opener, natural transitions — not by mechanical importance rank.
- `closing.open_question` is used only for child audiences when it fits (see [Writing for the ear](writing.md#children)).

The plan is internal scaffolding; listeners never see it. Scripts may realize it freely in structure and wording, but not in facts.
