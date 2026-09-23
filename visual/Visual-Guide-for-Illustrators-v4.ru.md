# Ұлы Дала Ғаламы / Вселенная Великой степи / Great Steppe Universe

## Visual Guide v4 — руководство для генерации и утверждения иллюстраций

> **Migration status: PARTIALLY MIGRATED.** Производственные правила перенесены
> в `ILLUSTRATION-PRODUCTION-GUIDE.md`; правила конкретных ветвей — в отдельные
> branch-guides. Этот файл остаётся legacy-источником полного текста,
> шаблонов, примеров и проверяемых формулировок до отдельной проверки миграции.

**Статус:** рабочая обновлённая версия для человеческой проверки  
**Назначение:** основа технических заданий, промптов, референс-пакетов и проверки новых иллюстраций  
**Область:** DAIRN: GREAT STEPPE, Battles of the Great Steppe и Shared Universe Illustrations  
**Не заменяет автоматически:** `Visual-Guide-for-Illustrators-v3.ru.md`, [GREAT-STEPPE-UNIVERSE.ru.md](../GREAT-STEPPE-UNIVERSE.ru.md) или решения человека.

---

## 1. Purpose

Этот документ переводит Visual Guide v3 в воспроизводимый рабочий процесс для художника и генеративной модели. Он соединяет три разные вещи, не подменяя одну другой:

```text
Historical Reference → проверяемые ограничения деталей
DAIRN Interpretation → современное художественное решение
DAIRN Visual Reference → внутренняя преемственность проекта
```

**FACT.** Исторические материалы, источники и статусы прав собраны в [`HISTORICAL-VISUAL-FOUNDATION.md`](HISTORICAL-VISUAL-FOUNDATION.md). V3 остаётся источником визуальной архитектуры; этот документ не объявляет новые канонические свойства мира.

**INFERENCE.** Генеративная модель должна получать не один общий стилевой ярлык, а структурированное задание: ветвь, роль изображения, исторические ограничения, канон, сцену и проверяемые запреты.

## 2. The Core Rule

> Источники устанавливают факты.  
> DAIRN интерпретирует.  
> Модель создаёт вариант.  
> Человек решает.

Нельзя представлять новую сгенерированную иллюстрацию как исторический документ, реконструкцию с гарантированной точностью или произведение Шевченко, Залесского либо Валиханова.

## 3. Source Hierarchy and Evidence Labels

| Layer | Meaning | Permitted use in an illustration brief |
| --- | --- | --- |
| `FACT` | подтверждён источником или каноническим документом | обязательное ограничение, если относится к сцене |
| `INFERENCE` | проектный вывод из источников | художественная рекомендация; может быть изменена человеком |
| `OPEN QUESTION` | данных или решения недостаточно | не превращать в точное требование; вынести на утверждение |
| `Historical Reference` | исторический материал с происхождением | проверка пространства, одежды, предметов, архитектуры, позы, композиционного наблюдения |
| `DAIRN Interpretation` | современная авторская переработка | новое изображение, в том числе сгенерированное |
| `DAIRN Fiction` | вымышленное содержание мира | сюжет, герои, существа и магия; не историческое доказательство |
| `DAIRN Visual Reference` | внутренний художественный ориентир | преемственность силуэтов, отношений, настроения и композиционного языка |

**FACT.** Нельзя делать переход `DAIRN Fiction → Historical Reference` или `DAIRN Interpretation → Historical Reference`.

## 4. One World, Three Visual Uses

| Use | Narrative role | Composition | Light and colour | Fantasy layer |
| --- | --- | --- | --- | --- |
| `DAIRN` / tabletop | мир существует независимо от игроков | наблюдательная; у человека есть пространство вокруг | естественный, рассеянный; приглушённая акварель | обнаруживается постепенно |
| `Battles` / computer chronicle | момент, достойный хроники | сюжетная; ясный визуальный центр и направление действия | выразительный, но не обязательно тёмный; акварель + гуашь | заметнее, но вырастает из Степи |
| `Shared` | общий образ одного мира | спокойная сцена с возможностью двух прочтений | умеренный контраст, естественный свет может быть выразительным | неоднозначный и ненавязчивый |

**FACT.** Различие не сводится к «DAIRN светлый, Battles тёмный». Обе ветви показывают одну Степь; различается способ рассказа.

## 5. Historical Grounding for Generation

### 5.1. What each corpus is for

| Corpus | Use it to check | Do not use it to claim |
| --- | --- | --- |
| Тарас Шевченко, казахстанская графика | человек и стоянка в ландшафте, дорога, очаг, юрты, берег, каменистый рельеф, масштаб пространства | универсальный костюм для всех мест и времён; готовый DAIRN-стиль |
| Бронислав Залесский, *La vie des steppes kirghizes* | отношения текста и листа, офортную архитектуру кадра, степное пространство, мотивы юрт и памятных мест | непосредственную натурную запись без художественной переработки |
| Шокан Валиханов, рисунки и зарисовки | позы, одежду, головные уборы, коней, предметы, стоянки, архитектурные и экспедиционные наблюдения | прямой перенос реального человека или регионально специфической детали на вымышленного героя |

### 5.2. Non-negotiable historical checks

Если сцена претендует на материально-культурную достоверность, до генерации выбрать релевантные исторические референсы и проверить:

1. место, сезон и рельеф;
2. одежду, обувь, головной убор и украшения;
3. оружие и способ его ношения;
4. конское и сокольничье снаряжение, если оно показано;
5. утварь, огонь, временную стоянку или юрту;
6. правдоподобие жеста, позы и взаимодействия человека с предметом.

**OPEN QUESTION.** Если для точной детали нет источника, задание должно говорить `не утверждать историческую точность`, а не восполнять пробел эффектным «этно-фэнтези».

### 5.3. Yurt is a construction check, not a decoration

Юрта проверяется по [YURT-VISUAL-SPEC.md](YURT-VISUAL-SPEC.md):
конструкция сохраняется при любом профиле изображения.

## 6. Canon and Character Boundaries

**FACT.** Иллюстрация должна сохранять канонические признаки и отношения героев, когда они заданы в локальном пилоте. Из игровых характеристик не выводится внешность.

Для `First Trial`:

| Element | Working visual boundary |
| --- | --- |
| Айбике | молодая наблюдательная степная лучница и всадница; действие и наблюдение, не позирование |
| Қарашаш | молодая опытная воительница; собранность, практическая оценка риска, не карикатурная агрессия |
| Ерсін | охотник, сокольничий и разведчик; практическое наблюдение, сокол и следы среды, не мистический пророк |
| Корсак | природный зверь в историческом контексте; в вымышленном эпизоде может быть сюжетным или призрачным, но это должно быть явно `DAIRN Fiction` |
| Сокол | птица сокольничьего; снаряжение и взаимодействие проверяются отдельно, если претендуют на историческую конкретность |

**FACT.** Ерсін появляется в третьей главе First Trial. Обложка с тремя героями допустима как обещание всей истории, но не должна быть подписана как иллюстрация единственной ранней сцены.

## 7. Visual Reference: the Supplied Tabletop Cover

**FACT.** Рабочая обложка, предоставленная 2026-09-21, показывает три фигуры, лучницу с луком, сокола, корсака, ковыль, горный горизонт и широкое небо. Это `DAIRN Visual Reference` и `DAIRN Interpretation`, а не Historical Reference.

**INFERENCE.** Для будущей настольной обложки полезно сохранять: ясную различимость трёх силуэтов, связь персонажей с ковылём и рельефом, спокойную акварельно-графическую поверхность, животное как часть среды и большое небо. Это не требует копировать композицию или позы.

**OPEN QUESTION.** До утверждения нового обложечного изображения отдельно сверять лук, одежду, украшения, меховые элементы и сокольничье снаряжение с релевантным набором источников.

### 7.1. Target Battles reference: `Блеск в ковыле`

**FACT.** `books/battles-of-the-great-steppe-pilot/stories/first-trial/artwork/chapters/chapter-01.png` — действующая обложка истории и иллюстрация её первой главы.

Для следующей утверждаемой версии использовать следующий внутренний `Battles Visual Reference`:

- синяя и бордовая героини различимы в движении;
- верховая мобильность и соревнование читаются до начала сверхъестественных событий;
- мониста — малый материальный сюжетный знак с естественным солнечным отблеском;
- степь, ветер и поздний свет участвуют в действии;
- кадр строит событие, а не нейтральный портрет персонажей.

**INFERENCE.** При создании родственных Battles-иллюстраций допустимо наследовать эти принципы, но не копировать кадр, позы или декоративные детали упряжи. Для DAIRN-версии той же ситуации следует вновь выбрать наблюдательную композицию по правилам раздела 10.1.

**FACT.** Сгенерированный вариант этой сцены будет `DAIRN Interpretation`, а не `Historical Reference`; любая точная материальная претензия должна возвращаться к историческому референс-пакету и четырём проверкам из раздела 13.

**OPEN QUESTION.** На момент последней проверки V2/V3-файлы не находятся в рабочем дереве. До их повторного сохранения текущий `chapter-01.png` не следует описывать как реализацию этого целевого референса.

## 8. Illustration Brief: Required Inputs

Каждое задание модели или художнику должно быть заполнено до генерации.

```yaml
asset_id: string
branch: DAIRN | BATTLES | SHARED
publication: tabletop | computer | both
asset_role: cover | chapter | character | location | encounter | object | handout
story_scope: canonical event | possible path | general-world scene
scene_summary: one or two sentences
characters: canonical IDs, or none
historical_reference:
  - source URL and exact work title
historical_checks:
  - landscape / clothing / object / architecture / pose
dairn_visual_reference:
  - internal image or approved traits
fiction_layer: none | subtle | explicit
must_show: list
must_not_show: list
unknowns_for_human_decision: list
rights_status_of_references: verified | review_required
```

Правило заполнения: если поле `historical_reference` пусто, нельзя называть итог «исторически точным». Если `unknowns_for_human_decision` не пусто, генерация может быть только исследовательским вариантом, не финалом.

## 9. Prompt Assembly Protocol

### 9.1. Prompt order

Собирать промпт в таком порядке:

1. роль и ветвь;
2. сцена и отношение человека к Степи;
3. подтверждённые материальные ограничения;
4. канонические персонажи и их действие;
5. визуальная композиция, свет и палитра;
6. допустимый слой DAIRN Fiction;
7. запреты и статус результата.

### 9.2. Base prompt template

```text
Use case: historical-scene / illustration-story
Asset type: [cover / chapter illustration / computer-game scene]
Branch: [DAIRN / Battles / Shared]
Narrative role: [what the viewer should understand or feel]
Scene: [place, season, time, action]
Historical grounding: [exact references and what they constrain]
Characters: [canonical traits and visible action]
Composition: [branch-specific camera, scale, negative space]
Light and palette: [branch-specific conditions]
Medium: handcrafted watercolour; [add gouache only for Battles where needed]
Fiction layer: [none / subtle / explicit and clearly fictional]
Must show: [list]
Must avoid: [list]
Constraints: contemporary DAIRN interpretation, not an archival image, no text, no logo, no watermark
```

### 9.3. Negative constraints

Всегда добавлять только релевантные запреты из этого списка:

- no generic European high fantasy; no castles, gothic towers, imported runes or ornamental armour;
- no glossy 3D render, anime, sterile concept-art finish or photorealistic fashion editorial;
- no generic nomad costume collage; no unverified ceremonial costume presented as everyday fact;
- no pseudo-historical archive treatment, false dates, museum labels or claims of authenticity;
- no yurt violating [YURT-VISUAL-SPEC.md](YURT-VISUAL-SPEC.md);
- no magic effects unless the brief declares an explicit fictional layer;
- no character posing for the viewer when the branch is DAIRN;
- no text, logo or watermark unless separately designed and proofread by a human.

## 10. Branch-specific Prompt Rules

### 10.1. DAIRN / tabletop

Use for exploration, travel, observation, quiet danger, possessions, encounters and possible paths.

- prefer wide or medium-wide framing;
- preserve substantial terrain and sky around people;
- use natural, diffuse, morning/evening or weather-based light;
- keep palette in grass, earth, ochre, stone, faded green and pale blue;
- show use, dust, fatigue and practical movement;
- reveal fantasy by trace, consequence or ambiguity before spectacle.

**Prompt cue:** `the steppe remains visually independent of the adventurers; the figures are part of a lived landscape`.

### 10.2. Battles / computer chronicle

Use for decisive action, turning points, character moments, threats and the promise of a continuing chronicle.

- establish a legible visual centre and directional action;
- allow foreground/middle-ground/background to carry story;
- use richer local colour and selective gouache density;
- allow expressive light, while keeping the landscape materially grounded;
- make hands, faces, gear and silhouette readable where the story needs them;
- let the fantastic grow from steppe weather, land, memory or threat rather than imported fantasy symbols.

**Prompt cue:** `a moment worthy of a chronicle, with the steppe actively shaping the event`.

### 10.3. Shared Universe Illustration

Use for yurt interiors, hearths, road, rest, memory, uncertain omens and common world imagery.

- avoid a frame that fixes one mutually exclusive outcome;
- retain moderate contrast and handmade watercolour;
- create two valid readings: observation for DAIRN and potential story-significance for Battles;
- do not recolour, darken or redraw the asset just to force different branch labels.

## 11. Covers Are Not Chapter Stills

Cover art may synthesize the promise of a whole book, module or computer chapter. It may bring together characters, an animal, a landscape and a symbolic object that are separated in story time.

It must nevertheless:

1. avoid asserting that the assembled image was a literal witnessed event;
2. preserve the narrative order in accompanying captions and metadata;
3. state `DAIRN Interpretation` in internal records;
4. receive an independent historical-material check for every visible concrete detail;
5. leave enough uncluttered space for later typography if the asset is a cover.

## 12. Generation Workflow

```text
1. Human selects branch, story scope and publication
2. Researcher selects source-backed constraints
3. Human resolves OPEN QUESTION items or marks the output exploratory
4. Author writes the structured brief
5. Model generates a variant labelled DAIRN Interpretation
6. Reviewer performs historical, canon, profile and publication checks
7. Human approves, revises or rejects
```

The model must not proceed from a reference image alone when the output claims a real material detail. A source-backed note must accompany the reference package.

## 13. Four Required Reviews

| Review | Questions |
| --- | --- |
| `Historical check` | Are claimed material details tied to suitable sources? Are geography and period limits retained? |
| `Canon check` | Are character identity, story order, world rules and yurt construction respected? |
| `Profile check` | Does the image read as DAIRN, Battles or Shared for reasons beyond brightness/darkness? |
| `Publication check` | Is the asset labelled as generated interpretation? Are source-file rights, platform rules and attribution requirements checked? |

No review can be replaced by a high aesthetic score from the model.

## 14. Acceptance Checklist

- [ ] Branch and `asset_role` are explicit.
- [ ] Narrative scope does not misstate the book or game event.
- [ ] Every historical claim has a source or is marked `OPEN QUESTION`.
- [ ] Historical sources are not copied, altered or passed off as DAIRN art.
- [ ] DAIRN Fiction is visible as fiction when it appears.
- [ ] Characters retain approved identity and relationships.
- [ ] Landscape is a real actor in the image, not generic wallpaper.
- [ ] Clothing, gear, animals and architecture have passed the relevant material check.
- [ ] Yurt construction meets [YURT-VISUAL-SPEC.md](YURT-VISUAL-SPEC.md) when shown.
- [ ] The intended branch reads without depending on a logo.
- [ ] The image contains no accidental text, watermark, invented heraldry or pseudo-archive claim.
- [ ] Rights for any source reproduction are separately checked.
- [ ] A human has made the final decision.

## 15. Prohibited Uses of Generative AI

Generative AI must not:

- alter, complete or colourize historical images for use as historical evidence;
- create an image that can be mistaken for an archival document;
- replace a named historical person with a DAIRN character inside an historical artwork;
- use a historical scan whose digital-rights status is unknown as a publication asset;
- resolve a canon question, source attribution or legal status by visual plausibility;
- generate new artwork in an issue that explicitly prohibits generation.

Any newly generated image belongs only to `DAIRN Interpretation` or `DAIRN Fiction`.

## 16. Minimum Metadata for a Generated Asset

```yaml
asset_id: draft-first-trial-cover-01
classification: DAIRN Interpretation
branch: DAIRN
publication_target: tabletop
source_constraints:
  - historical source title + URL
  - historical source title + URL
visual_references:
  - internal reference description
fiction_level: explicit
generator: model and date
human_decision: pending
publication_rights: pending review
```

This metadata is a working record, not a new runtime schema and not a replacement for a human rights review.

## 17. Short Production Cards

### A. Tabletop chapter illustration

```text
Branch: DAIRN
Goal: player-facing observation of the steppe before a choice
Frame: wide; people small enough for the land to remain legible
Light: diffuse autumn daylight
Historical focus: route, vegetation, practical clothing and tack
Fiction: one ambiguous trace only
Avoid: hero poster, visible magic, generic fantasy costume
```

### B. Computer-chronicle scene

```text
Branch: Battles
Goal: a decision or confrontation carries the story forward
Frame: visual centre, clear action direction, readable faces and hands
Light: expressive but natural to the weather and place
Historical focus: landscape and usable equipment
Fiction: declared threat may be visible
Avoid: darkness as a substitute for drama; European-fantasy symbols
Reference precedent: First Trial / `Блеск в ковыле` — две всадницы замечают
малую монисту в ковыле; наследовать принцип, а не копировать кадр
```

### C. Shared yurt interior

```text
Branch: Shared
Goal: an everyday scene that may later read as memory or omen
Frame: hearth, open shanyrak, human-scale quiet action
Light: natural top light and smoke path
Historical focus: yurt construction per YURT-VISUAL-SPEC.md and domestic objects
Fiction: ambiguous, optional
Avoid: violations of YURT-VISUAL-SPEC.md, fixed plot outcome
```

## 18. Human Decision Boundary

The following always remain human decisions:

- final canon and identity of characters;
- whether a reference is sufficiently relevant to a claimed detail;
- whether a generated variant fits the project aesthetically;
- release, attribution, platform compliance and legal-risk acceptance;
- whether a visual contradiction is accepted, changed or documented;
- the choice to use, reject or regenerate any asset.

---

## 19. Operational Summary

```text
Choose the branch.
Name the story role.
Ground concrete details in sources.
Separate fact from DAIRN interpretation and fiction.
Generate a labelled draft.
Review four dimensions.
Human decides.
```

**Canonical continuity:** one world, one memory, many possible paths — shown through different visual modes, never through false historical claims.
