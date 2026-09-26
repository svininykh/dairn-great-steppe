---
chapter-id: chapter-01
story-version: 0.2
language: ru
start: autumn-ride
title: Блеск в ковыле
---

<!--
Адаптация пилотной карты «Блеск в ковыле» для DAIRN Story Player.
Источник: Pilot-Map-01.md проекта Battles of the Great Steppe, версия 1.0.0.
Сюжетный результат сохранён: мониста остаётся у корсака, а Айбике и Қарашаш
продолжают погоню вдали от соседних аулов.
-->

# Осенний выезд {#autumn-ride}

:::scene
mood: calm
time: day
:::

Осенний ковыль серебрится под солнцем второй половины дня. За спиной остаются соседние аулы, впереди лежат знакомые пастбища и невысокие гряды, по которым девушки ездили с детства.

Айбике и Қарашаш происходят из одной семьи и одного рода. Они знают друг друга слишком давно, чтобы обычная поездка обошлась без состязания.

:::dialogue
speaker: karashash
:::
Ты опять изучаешь каждую травинку? Так можно пропустить всю степь.
:::

:::dialogue
speaker: aibike
:::
Зато я замечу то, мимо чего ты проскачешь.
:::

:::choice
id: ride_on_firm_ground
icon: leave
goto: broad-steppe
:::
Прибавить ходу по твёрдой земле
:::

:::choice
id: watch_the_grass
icon: inspect
goto: side-trail
:::
Осмотреть примятый ковыль
:::

# Простор впереди {#broad-steppe}

:::scene
mood: joy
time: day
:::

На открытом месте кони идут легко. Қарашаш первой пускает своего коня вскачь, и Айбике принимает молчаливый вызов. Расстояние между ними то сокращается, то снова растёт.

:::dialogue
speaker: karashash
:::
Не отставай. Мне не хочется возвращаться за тобой.
:::

В этот миг справа от тропы вспыхивает короткий золотой отблеск. Обе всадницы одновременно поворачивают головы.

:::choice
id: name_the_glimmer
icon: talk
goto: found-glimmer
:::
Указать на блеск
:::

:::choice
id: turn_without_warning
icon: attack
goto: found-glimmer
:::
Сразу повернуть коня
:::

# След в стороне {#side-trail}

:::scene
mood: mystery
time: day
:::

Между стеблями тянется узкая полоса примятой травы. На сухой земле сохранились мелкие отпечатки лап. Зверёк прошёл здесь недавно и двигался не к аулам, а в сторону дальних гряд.

:::effect
set-flag: extra-trail-found
set-variable: route=detour
:::

:::memory
event: extra-trail-discovered
:::

:::dialogue
speaker: aibike
:::
Свежий след. Идёт от низины к грядам.
:::

:::dialogue
speaker: karashash
:::
Потом разберёмся. Посмотри туда.
:::

Солнечный луч отражается от чего-то, лежащего в ковыле впереди.

:::choice
id: remember_the_tracks
icon: inspect
goto: found-glimmer
:::
Запомнить след и ехать к блеску
:::

# Находка в ковыле {#found-glimmer}

:::scene
mood: mystery
time: day
:::

В траве лежит мониста — женское украшение с рядом металлических подвесок. Оно не похоже на вещи из соседних аулов. Тонкая цепочка зацепилась за сухой стебель, словно находку потеряли совсем недавно.

Айбике и Қарашаш замечают её одновременно. На несколько мгновений обе замирают, а затем направляют коней к одной точке.

:::memory
event: monisto-discovered
:::

:::dialogue
speaker: aibike
:::
Я увидела её первой.
:::

:::dialogue
speaker: karashash
:::
Тогда постарайся первой до неё добраться.
:::

:::choice
id: choose_short_way
icon: attack
goto: rough-ground
:::
Срезать путь через кочки
:::

:::choice
id: choose_fast_way
icon: leave
goto: firm-route
:::
Обойти по твёрдой земле
:::

:::choice
id: choose_animal_trail
icon: inspect
condition: flag:extra-trail-found
goto: animal-route
:::
Использовать замеченную звериную тропу
:::

# Через кочки {#rough-ground}

:::scene
mood: tension
time: day
:::

Напрямик ближе, но земля здесь мягкая. Конь теряет скорость между кочками, и каждый неверный шаг грозит обернуться падением.

:::effect
set-variable: route=short
:::

:::check
stat: dexterity
difficulty: 8
success: aibike-first
failure: karashash-first
:::

# По твёрдой земле {#firm-route}

:::scene
mood: tension
time: day
:::

Обход делает путь длиннее, зато копыта уверенно ложатся на сухую землю. Скорость удаётся сохранить, и мониста быстро приближается.

:::effect
set-variable: route=fast
:::

:::choice
id: finish_fast_route
icon: leave
goto: aibike-first
:::
Не сбавлять хода
:::

# Звериная тропа {#animal-route}

:::scene
mood: mystery
time: day
:::

Примятая полоса проходит между кочками и выводит почти прямо к находке. Тот, кто оставил след, уже побывал возле монисты, но почему-то не унёс её.

:::effect
set-variable: route=detour
:::

:::dialogue
speaker: karashash
:::
Не самый прямой путь. Но сегодня тебе повезло.
:::

:::choice
id: emerge_from_trail
icon: take
goto: aibike-first
:::
Выйти к монисте по следу
:::

# Первая у находки {#aibike-first}

:::scene
mood: joy
time: day
:::

Айбике оказывается впереди. Подвески монисты блестят у самых копыт, и достаточно только наклониться, чтобы поднять её.

:::effect
set-variable: first-to-monisto=aibike
:::

:::memory
event: monisto-race-decided
:::

:::dialogue
speaker: aibike
:::
Кажется, спор окончен.
:::

:::choice
id: reach_for_monisto
icon: take
goto: corsac-takes-monisto
:::
Протянуть руку к монисте
:::

# Қарашаш впереди {#karashash-first}

:::scene
mood: tension
time: day
:::

На неровной земле теряются драгоценные мгновения. Қарашаш обходит опасное место и первой направляет коня к украшению.

:::effect
set-variable: first-to-monisto=karashash
:::

:::memory
event: monisto-race-decided
:::

:::dialogue
speaker: karashash
:::
Увидеть первой — ещё не значит получить.
:::

:::choice
id: refuse_to_yield
icon: refuse
goto: corsac-takes-monisto
:::
Не уступать находку
:::

# Рыжая молния {#corsac-takes-monisto}

:::scene
mood: tension
time: day
:::

Ковыль возле монисты вздрагивает. Из травы выскакивает корсак — небольшой, пыльно-рыжий, с настороженными ушами.

Прежде чем кто-либо успевает поднять монисту, зверёк хватает цепочку зубами. Подвески звякают, мониста исчезает в траве вместе с рыжим хвостом.

:::effect
set-flag: corsac-has-monisto
:::

:::memory
event: corsac-took-monisto
:::

:::dialogue
speaker: aibike
:::
Он унёс её!
:::

:::dialogue
speaker: karashash
:::
Вот и поспорили, кому она достанется.
:::

Корсак отбегает на несколько десятков шагов и на мгновение останавливается. Он не выглядит испуганным — скорее проверяет, последуют ли за ним.

:::choice
id: pursue_at_once
icon: attack
goto: swift-pursuit
:::
Немедленно броситься в погоню
:::

:::choice
id: study_escape_route
icon: inspect
goto: careful-pursuit
:::
Проследить направление его бега
:::

# Быстрая погоня {#swift-pursuit}

:::scene
mood: tension
time: day
:::

Кони срываются с места. Корсак исчезает в высокой траве, но редкий звон подвесок выдаёт его путь. Несколько раз кажется, что расстояние сокращается, однако зверёк каждый раз меняет направление.

:::effect
set-variable: pursuit=immediate
:::

:::dialogue
speaker: karashash
:::
Не гони прямо на него! Нырнёт в нору — больше не увидим.
:::

:::dialogue
speaker: aibike
:::
Тогда держись рядом и не дай ему свернуть.
:::

:::choice
id: follow_monisto_sound
icon: leave
goto: edge-of-known-steppe
:::
Держаться за звоном монисты
:::

# Осторожная погоня {#careful-pursuit}

:::scene
mood: mystery
time: day
:::

Айбике на мгновение придерживает коня. Верхушки травы показывают путь лучше самого зверька: корсак огибает низины и направляется к дальнему краю знакомых пастбищ.

:::effect
set-variable: pursuit=measured
:::

:::dialogue
speaker: karashash
:::
Наконец-то ты решила сначала посмотреть.
:::

:::dialogue
speaker: aibike
:::
А ты наконец-то решила подождать.
:::

:::choice
id: intercept_near_ridge
icon: inspect
goto: edge-of-known-steppe
:::
Перехватить корсака у дальней гряды
:::

# У края знакомой степи {#edge-of-known-steppe}

:::scene
mood: mystery
time: day
:::

У дальней гряды корсак скрывается из виду. В примятом ковыле остаётся цепочка мелких отпечатков. Она ведёт прочь от соседних аулов, туда, где привычные тропы теряются среди незнакомых складок земли.

Айбике спешивается и касается свежего следа. Қарашаш остаётся рядом: спор о монисте не окончен, но теперь обе понимают, что возвращаться с пустыми руками никто не хочет.

:::dialogue
speaker: karashash
:::
Можно вернуться за людьми. Или разделиться и взять его с двух сторон.
:::

:::dialogue
speaker: aibike
:::
Пока мы вернёмся, след остынет. Продолжим вместе.
:::

Вдалеке над травой появляется рыжий хвост. На одно мгновение в лучах низкого солнца снова вспыхивает мониста.

:::choice
id: continue_the_chase
icon: agree
goto: beyond-auls
:::
Продолжить погоню
:::

# Дальше от аулов {#beyond-auls}

:::scene
mood: danger
time: day
:::

Айбике снова садится в седло. Каждая по-прежнему считает находку своей и винит другую в промедлении, но теперь их кони идут в одном направлении.

Корсак уводит Айбике и Қарашаш всё дальше от соседних аулов — туда, где обычная скачка начинает превращаться в первое настоящее испытание.

:::effect
set-flag: chapter-01-complete
set-variable: next-episode=corsac-chase-part-2
:::
