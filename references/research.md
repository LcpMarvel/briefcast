# Research and verification

## When research is mandatory

If the brief depends on what is currently true or recently happened — news, releases, prices, statuses, anything with "today", "latest", "this week" — research with the host's live web tools. Never produce time-sensitive content from model memory: a plausible invented news item is this skill's worst failure, worse than an honestly short brief.

Evergreen topics with no freshness requirement need no live research, but verify surprising or specific claims before stating them as fact.

## Searching

- Run several distinct queries rather than one; use the brief's primary language and, for international topics, English as well.
- Source priority: (1) official or primary material — announcements, filings, papers, official pages; (2) quality first-hand reporting; (3) reliable secondary coverage. Aggregators and rewrites are leads to the real source, not sources.
- Record every viable candidate in `sources.json` as you go, including ones you later cut — exclusion reasons are part of the record.

## Candidate record

```json
{
  "id": "src-1",
  "title": "Reusable launcher completes second flight",
  "source": "Reuters",
  "source_url": "https://example.com/reports/launcher-second-flight",
  "published_at": "2026-09-28T08:00:00Z",
  "retrieved_at": "2026-09-29T21:30:00+08:00",
  "topic": "space",
  "factual_summary": "What this source actually says, independent of its framing.",
  "verification": {
    "status": "verified",
    "notes": "confirmed independently by src-2"
  },
  "used": true,
  "exclusion_reason": null
}
```

- `published_at` only when the source states it; `retrieved_at` always, from the actual fetch time.
- `verification.status`: `verified` (independent confirmation), `single-source`, `contested` (sources disagree), `unverified`.
- `factual_summary` records claims, not the headline's spin.

## Verification

- Important, volatile, or contested facts are cross-checked against at least two independent sources before entering `facts.json` as `verified`. Two copies of the same wire story are not independent.
- `single-source` facts may appear in the brief marked `probable`, worded so the listener hears the attribution ("据 X 报道", "according to X").
- Contested or unconfirmed claims: downweight, state the uncertainty in the brief, or drop. Never launder a guess into a fact.
- Names, numbers, dates, titles, and quotes are the standard failure points; check them specifically.

## Fact record

```json
{
  "facts": [
    {
      "id": "fact-1",
      "statement": "The launcher completed its second orbital flight on 2026-09-28 and landed intact.",
      "confidence": "verified",
      "source_refs": ["src-1", "src-2"],
      "notes": null
    }
  ]
}
```

`confidence`: `verified` | `probable` | `unverified`. `unverified` facts do not enter scripts.

## Supplied sources

URLs the user supplied are primary material: read them in full and build the brief around them. Add more research only when asked, or when the supplied material leaves obvious gaps the user would expect filled. Supplied sources meet the same verification rules — supplied is not the same as verified.
