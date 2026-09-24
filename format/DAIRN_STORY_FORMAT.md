# DAIRN Story Format — recorded current practice

SPDX-License-Identifier: Apache-2.0

## Status and provenance

This is a formalized record made in Issue #5, not a claim that the format or
`.dairn` packages were created earlier. It is based on the supplied historical
`dairn-story-format-0.1.md` and the supplied *Battles of the Great Steppe*
pilot book. Markdown remains the authored master format.

The historical document describes a single localized `story.<language>.md`
source with front matter. The pilot instead has `book.yaml`, `story.yaml`, and
per-chapter Markdown files. It uses `story-version: 0.2` (not the historical
0.1), chapter front matter, and fenced `:::…` directives. The pilot has only
Russian narrative files; its manifests contain some multilingual display
titles. Its `chapter-01.notes.md` explicitly calls the `effect` syntax an
open question. These differences are recorded, not normalized.

## Content and metadata observed

`book.yaml` has stable `book-id`, `book-version`, display title, `start-story`,
and references to stories, cover, illustration catalog, memory events and
canon. It may also contain a structured `heroes` list: each hero has a stable
`id`, while `name` may be intentionally absent. `story.yaml` has `story-id`,
`story-version`, `start-chapter`, optional cover and a chapter list. Chapter Markdown front matter contains `chapter-id`,
`story-version`, `language`, `start`, and title.

Issue #24 extends the book manifest with optional `npcs` and per-character
`initial-state` in either `heroes` or `npcs`. See
[Character Initial State](CHARACTER_INITIAL_STATE.md) for the shared contract.
These authored starting facts are independent of chapter effects and session
state. Missing facts remain unspecified; they are not extracted automatically
from canon or narrative. The story directive syntax and story version are
unchanged.

Technical IDs are stable and are not localized. Equivalent localizations must
retain compatible scene, choice, and transition IDs. Human text, headings, and
dialogue may differ by language. A reader must select a language explicitly or
use a documented fallback; the package itself is not single-language.

## Story covers and chapter illustrations

Each story in a book may have its own independent cover illustration. The
story's `cover` field remains optional. Recommended layout:

```text
stories/<story-id>/
├── story.yaml
├── artwork/
│   ├── cover.png
│   └── chapters/
│       ├── chapter-01.png
│       ├── chapter-02.png
│       └── ...
└── chapters/
    └── ...
```

In `story.yaml`, image paths are relative to that story's directory:

```yaml
cover: artwork/cover.png
chapters:
  - id: chapter-01
    source: chapters/chapter-01.ru.md
    illustration: artwork/chapters/chapter-01.png
```

The image fields have distinct roles:

| Field | Role | Path base |
| --- | --- | --- |
| `book.yaml` → `cover` | Cover of the whole book | Book directory |
| `story.yaml` → `cover` | Cover of that story | Story directory |
| `story.yaml` → `chapters[].illustration` | Illustration of that chapter | Story directory |

An author may explicitly reuse an image across these fields, but a story
cover is not required to match the first chapter's illustration. The
recommended story cover path is `artwork/cover.png`; chapter illustrations
remain independent resources under `artwork/chapters/`.

## Markdown constructs observed in the pilot

| Construct | Form | Meaning |
| --- | --- | --- |
| Scene | `# Title {#scene-id}` | Stable scene anchor; following prose is scene text. |
| Scene data | `:::scene` | Observed `mood` and `time` attributes. |
| Dialogue | `:::dialogue` | Has `speaker`; body is a line of dialogue. |
| Choice | `:::choice` | Has `id`, optional `icon`, `goto`, optional `condition`; body is label. |
| Transition | `goto: scene-id` | Local target scene in the same chapter, as used by pilot. |
| Condition | `condition: flag:…` | Availability condition; full expression grammar is not established. |
| Check | `:::check` | `stat`, `difficulty`, `success`, `failure`. |
| Effect | `:::effect` | Observed `set-flag` and `set-variable`; exact grammar is open. |
| Memory | `:::memory` | References an event ID from `memory/events.yaml`. |
| AI insertion | `:::ai_insert` | Optional constrained dialogue slot; it must not change authored transitions or state. |

`canon/` documents world, characters, tone, initial knowledge and AI limits.
`memory/events.yaml` gives events stable IDs and metadata. These are book
resources, not a replacement for authored chapter Markdown.

## Unresolved or experimental areas

The supplied specification discusses story-level front matter but does not
define the pilot's multi-chapter manifests, `ai_insert`, all directive parsing,
condition expressions, or effects. Pilot notes identify effect syntax and
initial statistics as unapproved. Consumers must report unsupported constructs
rather than infer mechanics. No rule semantics are defined here; the external
DAIRN engine remains authoritative.

The representation of initial state is now defined by Issue #24; the pilot's
unapproved numeric statistics remain omitted. Defining their representation
does not approve their values or resolve the experimental effect grammar.

## License boundary

This specification is Apache-2.0. A book's texts, images, audio, fonts and
other resources retain their own licenses; the format license does not license
book content.
