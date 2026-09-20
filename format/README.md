# Формат DAIRN

Этот каталог содержит существующую документацию формата DAIRN, перенесённую
из репозитория `svininykh/dairn-storyteller-telegram-lab`. Материалы созданы
до текущего архитектурного анализа и перенесены без переработки.

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
исходного репозитория. Их Git blob ID и SHA-256:

| Файл | Git blob ID | SHA-256 |
| --- | --- | --- |
| `DAIRN_BOOK_PACKAGE.md` | `800f05d8c1331aa6cb738afb817e63eaefc87e31` | `de4e22bdb2a6cb6b2786d3aa59300d106a6c69b719e028a1969d4e3f27a16b21` |
| `DAIRN_STORY_FORMAT.md` | `731e6ecaf5ad14b4d53a2e6276f8e6f8971b3857` | `cb65dd6297051df7cfc5b0bb05e0513214c2c83935c48ae61d373216e5dcc739` |

Проверка `sha256sum format/DAIRN_BOOK_PACKAGE.md
format/DAIRN_STORY_FORMAT.md` сопоставляет локальные файлы с зафиксированной
версией источника без обращения к изменяемой ветке `main`.
