# Output contract

One execution produces one run directory holding the profile, intermediate artifacts, final scripts, and a manifest describing them. Downstream stages should need to read only `manifest.json` to locate and consume everything.

## Run directory

Create runs under `briefcast-runs/` in the user's current working directory unless the user or caller specified a location:

```text
briefcast-runs/<run-id>/
  brief.yaml            # normalized Brief Profile
  sources.json          # researched candidates, metadata, verification status
  facts.json            # verified fact statements with provenance
  content-plan.json     # language-neutral editorial plan
  brief.primary.md      # the core product
  brief.secondary.md    # optional second-language version
  manifest.json         # status, artifacts, warnings; kept current at every stage
```

`<run-id>` starts as `YYYYMMDD-HHMM-<slug>`, e.g. `20260929-0715-world-news`. For a new request, create the run directory with an exclusive `mkdir` (not `mkdir -p` on the final directory). If that name already exists, try `-2`, `-3`, and so on; stop on other creation errors. Never overwrite or automatically resume a colliding directory. Record the allocated directory name as `manifest.run_id`.

When the caller explicitly points at an existing run directory to resume, reuse it and keep its original `run_id`.

## Brief Profile

```yaml
topic: "world news worth knowing"
audience:
  description: "second-grade students in China, around 7 years old"
  is_child: true                  # derived from the description; gates children rules
research:
  freshness: "24h"                # 24h | 7d | any | free text
  item_count: 3                   # target, not a quota
  supplied_sources: []            # URLs the user provided
primary_language:
  code: "zh-CN"
  purpose: "knowledge"            # free text: knowledge, listening, update, ...
secondary_language:
  enabled: true
  code: "en"
  purpose: "listening"
  difficulty:                     # keep whichever form the user used
    lexile: 600                   # optional
    tolerance: 50                 # optional
    cefr: null                    # optional
    description: null             # natural-language difficulty, optional
target_duration_minutes: 10       # natural read-aloud duration of the primary script
output:
  scripts: true
  sources: true
  facts: true
```

Fields the user never mentioned take sensible defaults; do not ask about them (see the skill's question policy). `target_duration_minutes` governs the primary script — the secondary version may legitimately differ in length and records its own estimate.

## Manifest

```json
{
  "run_id": "20260929-0715-world-news",
  "status": "complete",
  "created_at": "2026-09-29T07:15:00+08:00",
  "updated_at": "2026-09-29T07:22:31+08:00",
  "topic": "world news worth knowing",
  "audience": "second-grade students in China, around 7 years old",
  "languages": {
    "primary": {
      "code": "zh-CN",
      "title": "小小世界新闻：大熊猫坐飞机，小盒子去月亮",
      "script": "brief.primary.md",
      "status": "reviewed",
      "estimated_duration_minutes": 9.5,
      "review": {"passed": true, "notes": []}
    },
    "secondary": {
      "code": "en",
      "title": "News for You: Pandas, a New Moon Crater, and a Tiny Wild Cat",
      "script": "brief.secondary.md",
      "status": "reviewed",
      "estimated_duration_minutes": 7.0,
      "difficulty_requested": {"lexile": 600, "tolerance": 50},
      "review": {"passed": true, "notes": []}
    }
  },
  "target_duration_minutes": 10,
  "items": [
    {"id": "item-1", "title": "Reusable launcher completes second flight", "source_refs": ["src-1", "src-2"]}
  ],
  "outputs": {
    "profile": "brief.yaml",
    "sources": "sources.json",
    "facts": "facts.json",
    "plan": "content-plan.json",
    "scripts": ["brief.primary.md", "brief.secondary.md"]
  },
  "source_references": [
    {"id": "src-1", "title": "...", "source": "...", "url": "https://..."}
  ],
  "stages": {
    "profile": "done", "research": "done", "verify": "done", "select": "done",
    "plan": "done", "write_primary": "done", "write_secondary": "done", "review": "done"
  },
  "warnings": [],
  "errors": []
}
```

- Every language entry carries its own `title` — display metadata for apps and covers, not part of the script. The script files themselves carry no heading; in audio, the spoken opening line does the title's job.
- `status`: `running` | `complete` | `partial` (some artifact failed, the rest usable) | `failed`.
- `stages.*`: `pending` | `running` | `done` | `skipped` | `failed`.
- `languages.*.status`: `pending` | `written` | `reviewed` | `failed`.
- Omit `languages.secondary` and its script from `outputs.scripts` when the secondary language is disabled; mark `stages.write_secondary` as `skipped`. Include every enabled language even before its script exists, initially with status `pending`.
- `warnings` carries honest disclosures: fewer items than requested, single-source facts, contested claims, difficulty treated as approximate.
- Write `manifest.json` as soon as the profile exists: overall status `running`, profile stage `done`, remaining enabled stages `pending`. Mark the active stage `running` before starting it and update it after completion. A resumed run returns to overall status `running`; any interrupted `running` stage is incomplete. Only set `complete` after every enabled language is `reviewed` and the packaging gate passes.

## Duration estimation

Estimate read-aloud duration from text length at a natural broadcast pace:

- Mandarin: ≈ 250 characters/minute (240–280)
- English: ≈ 150 words/minute (140–160)
- Other languages: their typical speaking rate; record the assumption used

Estimates are approximate; round them. Meet `target_duration_minutes` by adjusting the script (item count, depth per item) — never by racing through disclaimers.

## Review

Before marking a language `reviewed`:

- **Primary**: every item in the script traces to `content-plan.json` and every fact to `facts.json`; the body obeys the clean-text rules in [Writing for the ear](writing.md); no `must_not_overstate` constraint is violated.
- **Secondary**: additionally the difficulty and listening review in [Secondary language](secondary-language.md).

A failed review keeps the draft, records the failure, and leaves that language below `reviewed` — never mark `complete` over an unfinished review.

## Packaging gate

Prose rules erode under a struggling research session. Before setting `manifest.json` status to `complete`, run these checks mechanically — actually execute them against the files, don't recall them from memory:

1. **Speakable scripts.** Define `check_scripts` below and call it with the `script` paths of every enabled language in the manifest, from the run directory. For the default paths, use `check_scripts brief.primary.md` for primary-only output, or `check_scripts brief.primary.md brief.secondary.md` for bilingual output. It must return `0`; `1` means an empty or non-speakable draft, and `2` means the check could not run (including a missing enabled script). Fix the files or the execution error, then rerun; missing files are never a pass.
2. **Traceable sources.** In `sources.json`, every record with `used: true` has a `source_url` that is an exact article page — not `null`, not a bare domain (`^https?://[^/]+/?$`). A violation is fixed by finding the same story on a traceable source and swapping it in, or by excluding the candidate — and if that leaves an item unsupported, dropping the item with a warning. Never fix it by keeping the root URL.
3. **Language entries complete.** Every enabled language in `manifest.json` carries `code`, `script`, `title`, and `estimated_duration_minutes`.
4. **Container shapes.** `sources.json` is exactly `{"candidates": [ ... ]}`; `facts.json` is exactly `{"facts": [ ... ]}`. No other top-level shape.
5. **Reference integrity.** Every `source_refs` in `facts.json` and `content-plan.json` points to an existing source id; every `core_facts` in `content-plan.json` points to an existing fact id.

```sh
check_scripts() {
  [ "$#" -gt 0 ] || return 2
  for script in "$@"; do
    if grep -q '[^[:space:]]' "$script"; then
      :
    else
      [ "$?" -eq 1 ] || return 2
      printf '%s: empty script\n' "$script" >&2
      return 1
    fi
    # ponytail: syntax heuristic; editor notes and factual quality still need review.
    if grep -nE '^[[:space:]]*(#|[-+*][[:space:]]|[0-9]+[.)][[:space:]]|>|\||([-_][[:space:]]*){3,}$)|[*`]|(^|[^[:alnum:]])_[^_]+_|~~|https?://|www\.|\[[^]]*\]' "$script"; then
      return 1
    else
      [ "$?" -eq 1 ] || return 2
    fi
  done
  return 0
}
```

This syntax check catches common formatting and citation markers; the editorial review still enforces the full clean-text contract.

If a check cannot be made to pass, degrade honestly — fewer items, `partial` status, warnings — and say so in `manifest.json`. A gate that "passes" by re-running the check with the files unchanged was not run.

## Resume

When a run directory's `manifest.json` exists and `status` is not `complete`:

1. Read `manifest.json` and `brief.yaml`; check which artifacts exist.
2. Skip stages marked `done`; never repeat expensive completed work — above all research.
3. Continue from the first incomplete stage, reusing existing artifacts unless they are invalid.
4. Keep the original `run_id` and `created_at`; update `updated_at`.

Failure handling by stage:

- Research fails → do not fabricate; deliver only what is verifiable (fewer items + warning) or report failure.
- A source fails → switch to other reliable sources.
- Not enough quality material → fewer items with an explanation in `warnings`, or an honest `failed`.
- Secondary fails → primary stands; `status: partial` with the error recorded.
- Review fails → keep the draft, record it, do not pretend it passed.
