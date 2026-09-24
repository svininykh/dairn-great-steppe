# Initial profile sources — Issue #25

[Қазақша](initial-state-sources.kk.md) / [Русский](initial-state-sources.ru.md) / English

Rationale revision: `6`; book version: `0.8.3`.
When facts or decisions change, update all three versions together and
increment the shared revision number. Translation corrections do not change facts.

Profile `name`, `description`, and `notes` are localized in `kk`, `ru`, `en`;
technical values `Bulky`, `Riding horse`, IDs, and paths are not translated.
The author established exact ages at entry: Aibike is 18, Karashash is 23,
and Yersin is 21. These values are recorded in canon and profiles;
they are not inferred from images or chapter text.
All three ages are also stored as numbers in `initial-state.age`.

The profiles use `initial-state` from the
[current format](../../format/CHARACTER_INITIAL_STATE.md).
Story text takes priority, followed by observable details in illustrations;
item mechanics come only from Market. One heroine's appearance is not
evidence for the other's possessions. All three chapters and portraits
have been reviewed.

## Aibike: start of chapter 1

- [Aibike's canon](canon/characters/aibike.md): name, 18 years
  old, archer, rider, composite bow. Age is stored in `initial-state.age`; description stays outside state.
- [Chapter 1, “Open Steppe Ahead”](stories/first-trial/chapters/chapter-01.ru.md#broad-steppe):
  her own riding horse. Its name and statistics are unspecified.
- [Chapter 1 illustration](stories/first-trial/artwork/chapters/chapter-01.png)
  and [portrait](artwork/heroes/aibike.png): ornamented blue clothing,
  belt, dark braids, fur-trimmed hat with a feather, earrings;
  the scene also shows boots, bow, quiver with arrows, saddle, and bridle.
- [Chapter 2 illustration](stories/first-trial/artwork/chapters/chapter-02.png)
  confirms the bow and quiver again. [Chapter 2 text](stories/first-trial/chapters/chapter-02.ru.md#ranged-clash)
  describes shooting; [chapter 3](stories/first-trial/artwork/chapters/chapter-03.png)
  shows Aibike drawing her bow. Arrows are not counted.

## Karashash: start of chapter 1

- [Karashash's canon](canon/characters/karashash.md): name,
  23 years old, warrior. [Chapter 1](stories/first-trial/chapters/chapter-01.ru.md#broad-steppe)
  explicitly describes her own horse.
- [Chapter 1 illustration](stories/first-trial/artwork/chapters/chapter-01.png)
  and [her portrait](artwork/heroes/karashash.png): ornamented burgundy clothing
  with fur trim, burgundy headwear, dark braids, belt, earrings,
  her own bow and quiver with arrows. Boots, saddle, and bridle appear in the scene.
- [Chapter 2](stories/first-trial/artwork/chapters/chapter-02.png)
  confirms the carried bow and quiver. Neither numerical statistics nor
  additional starting weapons are inferred from her role in close combat.

## Yersin: entry in chapter 3

- [“The Falconer”](stories/first-trial/chapters/chapter-03.ru.md#meet-yersin):
  an unfamiliar hunter stands on the hilltop and gives his name.
  [Canon](canon/characters/yersin.md) confirms his occupations as hunter,
  falconer, and scout; he is 21 years old. Ownership of the peregrine remains unresolved.
- [Portrait](artwork/heroes/yersin.png): dark hair, moustache, short beard,
  ochre-brown clothing with fur trim, fur-trimmed hat, belt, falconry glove,
  and belt pouch. The pouch contents, slot costs, and game properties of
  these two items are unspecified.
- [Illustration of his entry chapter](stories/first-trial/artwork/chapters/chapter-03.png):
  a visible whip in his hand. It is included as equipment of Yersin's depicted
  appearance in this chapter; the text describes no separate acquisition.
  This establishes the item's presence and type, not its combat statistics.

## Market mapping

### Appearance: table result numbers

`initial-state.appearance` contains selected numbers from the
[8d10 table](../../dairn/tables/character-traits-8d10-master.md).
Below is the editorial mapping of visible features to table categories
before the remaining fields were filled randomly.

| Character | `skin` | `hair` | `face` | `clothing` |
| --- | ---: | ---: | ---: | ---: |
| Aibike | 4 | 2 | 1 | 3 |
| Karashash | 4 | 2 | 1 | 3 |
| Yersin | — | 9 | 8 | 7 |

The heroines' portraits show rosy cheeks, braids, prominent cheekbones,
and dressy ornamented clothing. Yersin has visible wavy strands at his
temples, sharp facial features, and simple outer clothing without ornament
on its main fabric; the latter is mapped to “Неказистая / Plain,” without
inferring wealth. Yersin's skin tone is not equated with tanning or
weathering: the lighting prevents a confident choice. `physique` was initially omitted
for all three: clothing conceals their bodies, and mounted scenes do not
provide a reliable indication of height. Speech, Virtue, and Flaw were not
determined from images. A dash denotes an omitted field, not a table value.

At the author's subsequent request, the remaining appearance fields were
filled using a random number generator: a separate Python
`secrets.randbelow(10) + 1` call for each field, without rerolls. Results
are stored in the book, not generated when reading it. These are newly
selected random facts, not inferences from illustrations:

| Character | Field | d10 result |
| --- | --- | ---: |
| Aibike | `physique` | 8 |
| Karashash | `physique` | 3 |
| Yersin | `physique` | 6 |
| Yersin | `skin` | 7 |

All five `appearance` categories are now filled. Speech, Virtue, Flaw,
and game statistics were outside the scope of this appearance completion.

### Items

The [current Market](../../dairn/player-book/equipment/equipment-values-and-market-master.md)
and its [reference table](../../dairn/tables/basic-equipment-master.md#оружие) were checked.

| Item | Definition and action before filling the profile | Profile parameters |
| --- | --- | --- |
| Each heroine's bow and quiver | Set already exists; applicability to a composite bow clarified without a bonus | `d6`, 2 slots, `Bulky` |
| Yersin's qamshy | No definition existed; needed for the weapon depicted in his entry chapter. A row was first added to Market and its localizations | `d4`, 1 slot |
| Yersin's glove and pouch | Descriptive entries without game statistics; no new mechanical definitions introduced | Slot costs, contents, and properties omitted |

The whip's `d4` is an authored DAIRN definition at the level of an unarmed
Attack; 1 slot is the cost of an ordinary item under the existing rules.
This is a minimal Market addition, not a reconstruction of statistics from
an image. Blast, range, bonuses, and special effects were not added.
Saddles and bridles are described with the horses: their slot costs are not
assigned to the owners' Inventory. Clothing is not designated as Armor.

## Discrepancies and excluded information

- In chapter 1 the text places the monisto in the grass, whereas the image
  shows it on a branch. In either case it does not yet belong to the heroines
  and is absent from their Inventory.
- Chapter 2 depicts the heroines without the headwear seen in chapter 1
  and the portraits. This does not justify removing it from their initial descriptions.
- Karashash's spear appears only in the chapter 3 illustration. Market already
  includes a spear (`d8`, 1 slot), but its presence at her chapter 1 entry is
  unconfirmed; it is omitted from initial Inventory. This does not assert its absence.
- Yersin is depicted mounted in the chapter 3 battle, but the first meeting's
  text says he is standing. A horse at entry is unconfirmed: the later scene
  does not replace the entry text. No horse companion was added.
- The portrait shows a bird on the glove, while chapter 3 metadata calls it
  “Yersin's saker falcon.” The text calls the bird a peregrine, and canon leaves
  ownership unresolved. Neither ownership nor species in metadata overrides
  the text; the peregrine is not added as a companion. The monisto stays with the bird.
- Visible bags and bundles on the horses do not reveal their contents;
  rations, water, money, hidden weapons, and Talismans are not invented.
- Combat consequences from chapters 2–3 are not carried into initial states.
  [Chapter 1 notes](stories/first-trial/chapters/chapter-01.notes.md)
  leave initial statistics unapproved. The difficulty of `dexterity` / `willpower`
  checks is not a character's DEX / WIL value.

No list is declared complete. Missing STR, DEX, WIL, Hit Protection, Armor,
Fatigue, injuries, and other information are not replaced with zeros or `false`.
Chapter texts, illustrations, and their metadata are preserved; only ages were updated in canon.
