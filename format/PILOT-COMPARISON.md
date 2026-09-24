# Сопоставление формата с пилотом

Этот отчёт фиксирует наблюдаемое сопоставление перенесённых документов с
распакованным пилотом
[`books/battles-of-the-great-steppe-pilot/`](../books/battles-of-the-great-steppe-pilot/).
В Issue #24 отчёт актуализирован для расширения первоначального состояния.

## DAIRN Book Package

| Наблюдаемое правило | Статус | Evidence в пилоте |
| --- | --- | --- |
| `.dairn` является ZIP-контейнером без оборачивающего каталога книги | MATCH | Исходный пакет открывается как ZIP; `book.yaml` и `dairn-package.yaml` находятся в корне. |
| Манифест пакета имеет формат `dairn-book-package`, версию `0.1` и entry point `book.yaml` | MATCH | `dairn-package.yaml`. |
| `book.yaml` задаёт начальную историю, а story manifest — начальную главу и источники глав | MATCH | `book.yaml` → `first-trial`; `stories/first-trial/story.yaml` → `chapter-01`; все три chapter source существуют. |
| Структурированные герои имеют стабильные уникальные ID | MATCH | `aibike`, `karashash`, `yersin` в `book.yaml`; дубликатов нет. |
| Первоначальное состояние принадлежит персонажу и допускает пропуски | MATCH | Частичные состояния `aibike`, `karashash` и пустое состояние `yersin`; проверяются локальными тестами формата. |
| ZIP path safety, реакция reader на неизвестную версию и runtime immutability | NOT TESTABLE | Пилот — статический артефакт; реализации reader и runtime state здесь отсутствуют. |
| Проверка дубликатов scene ID и отсутствующих `goto` targets | NOT TESTABLE | Документ требует поведения валидатора; в этом репозитории валидатор не переносился. |
| First-chapter consumer profile | NOT TESTABLE | Маршрут к `chapter-01.ru.md` наблюдаем, но поведение consumer не представлено. |

## DAIRN Story Format

| Наблюдаемое правило | Статус | Evidence в пилоте |
| --- | --- | --- |
| `book.yaml`, `story.yaml` и Markdown глав описывают пилот | MATCH | Файлы присутствуют по путям, названным в документе. |
| Пилот использует `story-version: 0.2`, chapter front matter и fenced `:::` directives | MATCH | Все три `chapter-*.ru.md` имеют front matter; директивы присутствуют. |
| Технические ID не локализуются | MATCH | `story-id`, `chapter-id`, scene/choice IDs имеют стабильные латинские значения при русскоязычном тексте. |
| Сцены, `scene`, `dialogue`, `choice`, `check`, `effect`, `memory` и `ai_insert` наблюдаются | MATCH | Они присутствуют в Markdown глав; `scene` использует `mood` и `time`, а `effect` — `set-flag`/`set-variable`. |
| Историческая модель одного `story.<language>.md` версии 0.1 | MISMATCH | Пилот имеет многоглавную структуру и `story-version: 0.2`; перенесённый документ уже фиксирует это расхождение. |
| Многоязычные narrative-файлы и documented language fallback | NOT TESTABLE | В пилоте есть только `*.ru.md`; fallback и другие локализации отсутствуют. |
| Полная грамматика condition/effect и rule semantics | NOT TESTABLE | Документ и `chapter-01.notes.md` оставляют эти вопросы открытыми; Engine не переносился. |

## Вывод

Расхождение с исторической однофайловой моделью зафиксировано, но не
исправлялось. Issue #24 добавляет общий контракт первоначального состояния
героев и NPC без изменения синтаксиса глав или устройства ZIP-контейнера.
