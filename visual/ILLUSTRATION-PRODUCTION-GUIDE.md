# Illustration Production Guide

**Scope:** общий процесс для `DAIRN-TABLETOP`, `BATTLES` и `SHARED`.
Он не устанавливает художественный язык ветви. Выберите его в
[VISUAL.md](VISUAL.md) и приложите соответствующее branch-guide.

## 1. Brief

До создания заполнить: `asset_id`, `branch`, `publication`, `asset_role`,
`story_scope`, краткое описание сцены, персонажей, исторические источники и
проверки, внутренний visual reference, слой fiction, обязательное/запрещённое,
нерешённые вопросы и статус прав источников.

Пустой historical reference запрещает называть результат исторически точным.
При нерешённых вопросах результат — исследовательский вариант, не финал.

## 2. Prompt assembly

Собирать в порядке: роль и ветвь → сцена и отношение к Степи → подтверждённые
материальные ограничения → персонажи и действие → правила выбранной ветви →
fiction layer → запреты/статус. Указать: современная интерпретация DAIRN, не
архивное изображение, без текста/логотипа/watermark.

Всегда применять лишь релевантные ограничения: no generic European high
fantasy; no glossy 3D/anime/sterile finish; no псевдоисторический архив;
no неверно построенная юрта; no magic без явно указанного fiction layer.
Дополнительные branch-ограничения берутся только из выбранного руководства.

## 3. Workflow и review

```text
Человек выбирает ветвь и роль → источники ограничивают детали →
человек фиксирует/отмечает unknowns → brief → вариант DAIRN Interpretation →
historical + canon + profile + publication review → human approval
```

| Проверка | Вопрос |
| --- | --- |
| Historical | Подтверждены ли заявленные материальные детали подходящими источниками? |
| Canon | Сохранены ли персонажи, порядок истории, правила мира и конструкция юрты? |
| Profile | Читается ли ветвь по роли, а не только по яркости? |
| Publication | Есть ли маркировка interpretation, проверка прав, атрибуции и правил площадки? |

## 4. Acceptance и metadata

Перед утверждением проверить: branch и asset role названы; scope не искажён;
каждое историческое утверждение имеет источник или `OPEN QUESTION`; fiction
виден как fiction; персонажи и ландшафт корректны; проверены релевантные
одежда/снаряжение/животные/архитектура; отсутствуют случайный текст, watermark,
выдуманная геральдика и псевдоархивность; финальное решение сделал человек.

Минимальные метаданные: `asset_id`, `classification: DAIRN Interpretation`,
`branch`, цель публикации, source constraints, visual references, fiction level,
generator/date, human decision, publication rights.

## 5. Ограничения Generative AI и решение человека

Нельзя изменять историческое изображение как доказательство, создавать ложный
архив, подменять в историческом произведении человека персонажем DAIRN,
публиковать источник с неясными digital rights или решать канон/атрибуцию/право
по визуальной правдоподобности. Генерация — только `DAIRN Interpretation` или
`DAIRN Fiction`.

Человек всегда решает канон, релевантность источника, эстетическое соответствие,
публикацию, атрибуцию, правовой риск и принятие/отклонение варианта.

## Миграция

| Legacy location | Эта локация |
| --- | --- |
| V4 §§1–3 | назначение, core rule, evidence labels |
| V4 §§8–9 | brief и prompt assembly |
| V4 §§11–19 | covers, workflow, reviews, checklist, AI limits, metadata, cards, human boundary |
| V4 §10 | только routing: детальные правила перенесены в branch-guides |

Источниковедческие правила и source register остаются в
[HISTORICAL-VISUAL-FOUNDATION.md](HISTORICAL-VISUAL-FOUNDATION.md).
