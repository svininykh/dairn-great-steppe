# DAIRN Book Package v0.1

SPDX-License-Identifier: Apache-2.0

## Scope

A `.dairn` is a portable distribution container around an authored DAIRN book.
It was introduced in Issue #5. It does not replace Markdown, define game
mechanics, or depend on StoryPlayer or Telegram implementation details.

## Physical format

The file extension is `.dairn`. Its bytes are a standard ZIP archive using
UTF-8 entry names and UTF-8 text files. Entries are relative slash-separated
paths; absolute paths, empty path components, and `..` are invalid. Unknown
safe files are preserved and ignored by readers that do not understand them.

Archive root contains no enclosing book directory. Required entries are:

```text
dairn-package.yaml
book.yaml
```

`dairn-package.yaml` is created by the packager:

```yaml
package-format: dairn-book-package
package-version: "0.1"
book: book.yaml
```

Readers must reject a package they cannot open, an absent manifest, another
format name, another package version, or another book entry point. Compatible
future versions may add optional fields and files; an incompatible version
must be reported, not guessed.

## Book layout

The supplied pilot is the baseline and contains:

```text
book.yaml
artwork/
catalogs/
memory/
canon/
stories/<story-id>/story.yaml
stories/<story-id>/chapters/*.md
stories/<story-id>/artwork/
```

Only `book.yaml` and the resources it references are required by this package
specification. The other directories are optional. `book.yaml` identifies the
starting story; its story manifest identifies the starting chapter and each
chapter source. A package reader must not assume every optional directory
exists.

`book.yaml` → `cover` identifies the whole book's cover relative to the book
directory (for example, `artwork/covers/book-cover.png`). Each story may also
have its own optional `story.yaml` → `cover`, recommended at `artwork/cover.png`
relative to that story's directory. This is independent of
`story.yaml` → `chapters[].illustration`, whose paths are also relative to the
story directory (for example, `artwork/chapters/chapter-01.png`). Authors may
explicitly reuse an image, but story covers need not match first-chapter
illustrations. See [Story covers and chapter illustrations](DAIRN_STORY_FORMAT.md#story-covers-and-chapter-illustrations)
for the recommended layout. This convention does not make story covers required.

## Structured heroes and NPCs

`book.yaml` may contain a `heroes` list. Every listed hero requires a stable,
unique `id`; `name` is optional and its absence is meaningful. A package reader
exposes this list as structured data and does not derive hero fields from prose
or other authored resources. The package is immutable at runtime: a name
provided by a reader belongs to a game session, not to this manifest.

Issue #24 adds an optional `npcs` list with the same character contract.
IDs must be unique across both lists. Existing `heroes` entries retain their
meaning; no migration to a new character registry is required.

Each hero or NPC may independently contain an optional `initial-state` mapping.
It records authored facts at that character's entry into the story, which need
not coincide with the opening chapter. An absent block, an empty `{}` block,
and partially or fully authored blocks are all valid. Unknown values must be
omitted, including nested values; readers must not supply defaults or derive
them from descriptions. `null` is not a representation of an unknown value.
There is no book-level `initial-state`.

The normative field contract, collection semantics and examples are in
[Character Initial State](CHARACTER_INITIAL_STATE.md). Hero and NPC state use
the same [schema](schemas/character-initial-state.schema.json). Character
description and identity remain separate from state. Creating or modifying
session state is the responsibility of an external consumer and never changes
the book's authored initial state.

This is an additive manifest extension; the ZIP package version remains `0.1`.
Books without these optional fields remain valid. Compatibility with any
particular older external reader must be verified in that reader's repository.

## Localized character text

Character `name`, `description`, and `notes`, plus item, talisman, and
companion `name` and `notes`, accept either a legacy nonblank string or a
nonempty map of nonblank translations keyed by `kk`, `ru`, and `en`.
Unknown translations are omitted; other locale keys and null values are
invalid. See the [localized text contract](CHARACTER_INITIAL_STATE.md#локализация-отображаемых-полей).
Display selects the requested language, then `kk`; if neither exists,
the field is unavailable. Legacy strings display unchanged. Validation
preserves the entire map and does not select or generate a translation.
Technical IDs, resource paths, kinds, and properties are not localized.
Existing books remain valid, but consumers must support translation maps
before loading localized books. The container version remains `0.1`.

## Minimal validation

Validate ZIP readability, safe paths, package manifest/version, `book.yaml`,
the start-story reference, story-source references, start-chapter references,
chapter-source references, and duplicate story/chapter IDs. This is deliberately
not a full narrative-schema or rules validator. Each present chapter is also
checked for duplicate scene IDs and `goto` targets absent from that chapter.

When validating the character extension, also check the state schema, unique
character IDs, companion references and explicitly supplied HP bounds. The
local `validate_characters.py` checks only this extension, not the full package
validation above; see [validation commands](README.md#проверки).

## First-chapter consumer profile

A consumer that only needs an opening-context image reads `book.yaml`, its
`start-story`, that story's `start-chapter`, then the chapter source for the
chosen language. It may use that chapter's authored text and explicitly
referenced canon as context, and stops after rendering the image. It must not
silently read later chapters or claim their events as current context.

For the supplied pilot this resolves to `first-trial` → `chapter-01` →
`stories/first-trial/chapters/chapter-01.ru.md`. The package nevertheless
contains all book resources unchanged.

## License boundary

This package specification is Apache-2.0. Content licenses remain independent
and must be carried in existing metadata or documented by the book publisher;
packaging never relicenses content.
