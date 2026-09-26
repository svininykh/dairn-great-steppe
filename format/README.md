# Формат DAIRN

Здесь описано, как оформить интерактивную книгу DAIRN.
Начните с [примера главы](DAIRN_CHAPTER_FORMAT.md#пример-минимальной-полной-главы):
скопируйте его, напишите сцены и добавьте файл в
[список глав истории](DAIRN_STORY_FORMAT.md#манифест-истории).

## Структура книги

`.dairn` — ZIP-архив. Внутри, например:

```text
dairn-package.yaml
book.yaml
stories/
└── journey/
    ├── story.yaml
    ├── artwork/
    └── chapters/
        └── chapter-01.ru.md
```

`book.yaml` задаёт начальную историю и персонажей (`heroes`, `npcs`,
их `initial-state`); `story.yaml` — начальную главу и список файлов глав.

| Что нужно | Где читать |
| --- | --- |
| Написать главу: сцены, реплики, выборы | [Формат главы](DAIRN_CHAPTER_FORMAT.md) |
| Собрать главы в историю, добавить иллюстрации | [Формат истории](DAIRN_STORY_FORMAT.md) |
| Описать состояние персонажей | [Поля персонажа](CHARACTER_INITIAL_STATE.md), [примеры](examples/character-initial-states.yaml) |
| Упаковать книгу в `.dairn` | [Пакет книги](DAIRN_BOOK_PACKAGE.md) |
| Посмотреть особенности пилота и происхождение документов | [Сопоставление с пилотом](PILOT-COMPARISON.md) |

Первые четыре документа — спецификации. Примеры и наблюдения пилота
не добавляют правил. «Экспериментально» означает, что запись ещё
уточняется; «Открытый вопрос» — что решение пока не принято.

## Что определяет формат

Формат задаёт поля, ID, связи сцен и пути ресурсов.
[Игровые правила](../dairn/README.md) определяют характеристики, броски,
Защиту, Броню, Урон и Поклажу. Движок выполняет проверки и эффекты,
выбирает язык интерфейса и хранит игровую сессию, не меняя авторские файлы.
О неподдерживаемых конструкциях движок должен сообщать.

## Проверки

Для персонажей есть [JSON Schema](schemas/character-initial-state.schema.json)
и Python-валидатор. Полной проверки пакета и глав пока нет: схемы
`dairn-package.schema.json`, `book.schema.json` и `story.schema.json`
можно добавить позже. Требования документации действуют и без схем.

`schemas/`, `examples/`, `tests/` — инструменты этого каталога;
включать их в книгу не требуется. Из корня репозитория, Python 3.10+:

```sh
python3 -m venv /tmp/dairn-format-venv
/tmp/dairn-format-venv/bin/python -m pip install -r format/requirements.txt
/tmp/dairn-format-venv/bin/python -B -m unittest discover -s format/tests -v
/tmp/dairn-format-venv/bin/python -B format/validate_characters.py books/battles-of-the-great-steppe-pilot/book.yaml
```

При установленных зависимостях можно использовать `python3` напрямую.
Валидатор проверяет только персонажей в распакованном `book.yaml`,
возвращает ненулевой код при ошибке и не изменяет данные.
