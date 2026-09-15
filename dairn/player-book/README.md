# Книга игрока

Рабочая структура Книги игрока **DAIRN: Ұлы Дала Ғаламы**, основанная
на механическом ядре Cairn 2e и адаптированная для мира DAIRN.

## Принцип подготовки и публикации

Для каждой локализуемой главы сохраняется единый мастер `*-master.md`.
Его основной язык — русский, а ключевые системные термины приводятся в
форме **Қазақша / Русский / English** по глоссарию DAIRN.

Публичные версии формируются отдельно:

- `*-kk.md` — қазақша;
- `*-ru.md` — русский;
- `*-en.md` — English.

Файл главы без языкового суффикса служит навигационной страницей и
содержит ссылки на рабочий мастер и публичные версии. Содержательные
изменения сначала вносятся в мастер, а затем синхронизируются с тремя
переводами. Для локализуемых таблиц используется тот же принцип; сами
таблицы остаются в каталоге [`../tables`](../tables/README.md) и не
дублируются внутри глав.

## Порядок разделов и глав

### Введение в игру

- [Введение, принципы и роли](introduction/overview-and-principles.md)

### Персонаж

- [Создание персонажа](character/character-creation.md)
- [Персонаж в игре](character/character-in-play.md)
- [Жизненные пути Великой Степи](character/life-paths-of-the-great-steppe.md)

### Опасность и Схватка

- [Схватка](danger-and-combat/combat.md)

### Серіктер / Спутники / Companions

- [Серіктер / Спутники / Companions](character/companions.md)

### Снаряжение

- [Снаряжение, ценности и рынок](equipment/equipment-values-and-market.md)

### Игра в мире

- [Правила игры](playing-in-the-world/game-procedures.md)
- [Путешествие](playing-in-the-world/travel.md)
- [Привал и длительные дела](playing-in-the-world/downtime.md)

### Необычное

- [Магия](supernatural/magic.md)

### Великая Степь

- [Игрок в мире Великой Степи](great-steppe/player-in-the-great-steppe.md)
- [Дала қатерлері / Угрозы Степи / Threats of the Steppe](great-steppe/threats-of-the-steppe.md)

### Справочные материалы игрока

- [Краткая памятка правил](player-reference/rules-reference.md)
- [Таблицы](player-reference/tables-reference.md)
- [Терминологическая памятка](player-reference/terminology-reference.md)

Общие таблицы хранятся в [`../tables`](../tables/README.md), а полная
терминологическая база — в [`../glossary.md`](../glossary.md).
