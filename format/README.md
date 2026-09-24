# Формат DAIRN

Этот каталог содержит существующую документацию формата DAIRN, перенесённую
из репозитория `svininykh/dairn-storyteller-telegram-lab`. Материалы созданы
до текущего архитектурного анализа и первоначально перенесены без переработки.
В Issue #24 документы дополнены контрактом первоначального состояния персонажа.

- [DAIRN Book Package](DAIRN_BOOK_PACKAGE.md) — исходный путь
  [`docs/DAIRN_BOOK_PACKAGE.md`](https://github.com/svininykh/dairn-storyteller-telegram-lab/blob/main/docs/DAIRN_BOOK_PACKAGE.md).
- [DAIRN Story Format](DAIRN_STORY_FORMAT.md) — исходный путь
  [`docs/DAIRN_STORY_FORMAT.md`](https://github.com/svininykh/dairn-storyteller-telegram-lab/blob/main/docs/DAIRN_STORY_FORMAT.md).

Документы можно сопоставлять с распакованным пилотом в
[`books/battles-of-the-great-steppe-pilot/`](../books/battles-of-the-great-steppe-pilot/).
Их архитектурный статус и границы слоя `FORMAT` продолжают исследоваться в
Issue #1; этот перенос не утверждает формат как окончательный.

## Проверяемое происхождение

Документы перенесены из commit
[`7513d33d116358750ec79ba7efea7c6677e57130`](https://github.com/svininykh/dairn-storyteller-telegram-lab/tree/7513d33d116358750ec79ba7efea7c6677e57130)
исходного репозитория. Git blob ID и SHA-256 исходных, доработкам предшествующих версий:

| Файл | Git blob ID | SHA-256 |
| --- | --- | --- |
| `DAIRN_BOOK_PACKAGE.md` | `800f05d8c1331aa6cb738afb817e63eaefc87e31` | `de4e22bdb2a6cb6b2786d3aa59300d106a6c69b719e028a1969d4e3f27a16b21` |
| `DAIRN_STORY_FORMAT.md` | `731e6ecaf5ad14b4d53a2e6276f8e6f8971b3857` | `cb65dd6297051df7cfc5b0bb05e0513214c2c83935c48ae61d373216e5dcc739` |

Эти суммы относятся к историческому источнику, а не к текущим документам,
изменённым в Issue #24.

## Первоначальное состояние

- [Контракт и соответствие планшету](CHARACTER_INITIAL_STATE.md).
- [JSON Schema](schemas/character-initial-state.schema.json).
- [Примеры заполнения](examples/character-initial-states.yaml).

## Проверки

Из корня репозитория, Python 3.10 или новее:

```sh
python3 -m venv /tmp/dairn-format-venv
/tmp/dairn-format-venv/bin/python -m pip install -r format/requirements.txt
/tmp/dairn-format-venv/bin/python -B -m unittest discover -s format/tests -v
/tmp/dairn-format-venv/bin/python -B format/validate_characters.py books/battles-of-the-great-steppe-pilot/book.yaml
```

При уже установленных зависимостях можно использовать `python3` напрямую.
Валидатор проверяет расширение персонажей распакованного `book.yaml` и
возвращает ненулевой код при ошибке. Это не полный валидатор пакета `.dairn`
или игровой механики. Тесты включают чтение манифеста из ZIP, старый формат
без состояния, примеры и текущий пилот; внешний Engine здесь не запускается.
