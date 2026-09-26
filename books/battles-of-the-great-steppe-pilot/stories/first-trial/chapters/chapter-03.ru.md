---
chapter-id: chapter-03
story-version: 0.2
language: ru
start: toward-high-ground
title: Ледяные крылья
---

# К возвышенности {#toward-high-ground}

:::scene
mood: mystery
time: evening
:::

На пути к возвышенности ветер становится непривычно холодным. По склону тянутся длинные тени.

:::choice
id: climb_high_ground
icon: leave
goto: meet-yersin
:::
Подняться к месту, где скрылся сапсан
:::

# Сокольничий {#meet-yersin}

:::scene
mood: tension
time: evening
:::

На вершине стоит незнакомый охотник. Сапсан опускается возле него с монистой в когтях. Қарашаш следит за руками незнакомца.

:::dialogue
speaker: aibike
:::
Эту монисту мы нашли. Верни её.
:::

:::memory
event: heroines-met-yersin
:::

:::dialogue
speaker: yersin
:::
Я Ерсін. Птица сама принесла украшение. Постойте, внизу что-то движется.
:::

:::ai_insert
id: yersin-first-dialogue
type: dialogue
character: yersin
optional: true
max-chars: 180
:::
Тише. Дайте послушать.
:::

Что ответит Айбике?

:::choice
id: ask_about_danger
icon: talk
goto: aibike-asks-danger
:::
«Где? Покажи, что ты заметил».
:::

:::choice
id: demand_monisto
icon: refuse
goto: aibike-demands-monisto
:::
«Сначала монисту. Мы за ней через всю степь скакали».
:::

# Взгляд вниз {#aibike-asks-danger}

:::scene
mood: tension
time: evening
:::

Айбике переводит взгляд на склон, но украшение из виду не выпускает.

:::dialogue
speaker: yersin
:::
В ковыле, у подножия.
:::

Қарашаш оглядывает склон.

Что спросит Қарашаш?

:::choice
id: karashash_asks_shelter
icon: inspect
goto: yersin-shows-shelter
:::
«Если нас прижмут здесь, куда отходить?»
:::

:::choice
id: karashash_questions_warning
icon: talk
goto: yersin-admits-uncertainty
:::
«Ты уже видел, кто там, или только слышал?»
:::

# Спор о находке {#aibike-demands-monisto}

:::scene
mood: tension
time: evening
:::

Айбике смотрит на монисту. Ерсін не отводит глаз от склона.

:::dialogue
speaker: yersin
:::
Она здесь. Не до неё сейчас.
:::

Қарашаш оглядывает склон.

Что спросит Қарашаш?

:::choice
id: karashash_asks_shelter_after_demand
icon: inspect
goto: yersin-shows-shelter
:::
«Если нас прижмут здесь, куда отходить?»
:::

:::choice
id: karashash_questions_warning_after_demand
icon: talk
goto: yersin-admits-uncertainty
:::
«Ты уже видел, кто там, или только слышал?»
:::

# Каменная сторона {#yersin-shows-shelter}

:::scene
mood: tension
time: evening
:::

:::dialogue
speaker: yersin
:::
К камням под склоном. Там можно укрыться.
:::

:::dialogue
speaker: karashash
:::
Айбике, слышала? Не отрывайся от нас.
:::

:::choice
id: watch_slope_after_shelter
icon: inspect
goto: pale-movement
:::
Посмотреть на склон
:::

# Что видел охотник {#yersin-admits-uncertainty}

:::scene
mood: tension
time: evening
:::

:::dialogue
speaker: yersin
:::
Видел, как расходится трава. Движутся сюда.
:::

:::dialogue
speaker: karashash
:::
Тогда смотрим вместе. Айбике, держись рядом.
:::

:::choice
id: watch_slope_after_warning
icon: inspect
goto: pale-movement
:::
Посмотреть на склон
:::

# Бледное движение {#pale-movement}

:::scene
mood: danger
time: evening
:::

Ковыль шелестит со всех сторон. Из него выходят корсаки — бледные, едва различимые в сумерках. Они движутся вровень друг с другом, окружая возвышенность.

:::memory
event: ghost-corsacs-appeared
:::

:::ai_insert
id: yersin-ghost-corsacs-dialogue
type: dialogue
character: yersin
optional: true
max-chars: 180
:::
Держитесь вместе. За теми, что уходят в дымку, не гонитесь.
:::

:::choice
id: form_shared_line
icon: agree
goto: ghost-pack
:::
Держаться вместе
:::

# Призрачная стая {#ghost-pack}

:::scene
mood: danger
time: evening
:::

Айбике стреляет по бледным силуэтам, а Қарашаш встречает первых прорвавшихся. Ерсін замечает новых зверей ещё в дымке.

:::effect
set-flag: yersin-joined
:::

:::choice
id: trust_yersin_warning
icon: agree
goto: icy-crows
:::
Следовать предупреждениям Ерсіна
:::

:::choice
id: force_way_out
icon: attack
goto: exposed-to-cold
:::
Попытаться прорваться через стаю
:::

# Ледяные вороны {#icy-crows}

:::scene
mood: danger
time: evening
:::

Над возвышенностью собираются чёрные птицы. С их первым ударом воздух белеет от инея, а трава под копытами становится ломкой.

:::memory
event: icy-crows-attacked
:::

:::ai_insert
id: yersin-crows-dialogue
type: dialogue
character: yersin
optional: true
max-chars: 180
:::
Под склон! Здесь мы открыты ветру.
:::

:::effect
set-variable: ice-tactic=shelter
:::

:::choice
id: move_under_slope
icon: leave
goto: final-stand
:::
Укрыться под склоном
:::

# Под ледяным ветром {#exposed-to-cold}

:::scene
mood: danger
time: evening
:::

Навстречу прорывающимся бьёт холод. Призрачные корсаки снова сходятся. Трое отступают к каменной стороне возвышенности.

:::effect
set-flag: touched-by-ice
set-variable: ice-tactic=forced-retreat
:::

:::ai_insert
id: yersin-retreat-dialogue
type: dialogue
character: yersin
optional: true
max-chars: 180
:::
К камням! Укроемся от ветра.
:::

:::choice
id: reach_stone_shelter
icon: agree
goto: final-stand
:::
Отойти к камням вместе
:::

# Общая позиция {#final-stand}

:::scene
mood: tension
time: evening
:::

В узком проходе трое сдерживают стаю. Под стрелами распадаются бледные силуэты; Қарашаш отбивает натиск тех, кто подобрался ближе. Наконец корсаки растворяются в сумраке. Но ледяной ветер по-прежнему бьёт в проход.

:::check
stat: willpower
difficulty: 6
success: threat-recedes
failure: endure-last-wave
:::

# Последняя волна {#endure-last-wave}

:::scene
mood: danger
time: night
:::

Ледяные вороны заходят ещё раз. Трое выдерживают удар за камнями, пока стая не поднимается выше.

:::effect
set-flag: difficult-icy-battle
:::

:::choice
id: wait_for_silence
icon: agree
goto: threat-recedes
:::
Дождаться, пока стихнет ледяной ветер
:::

# После нападения {#threat-recedes}

:::scene
mood: relief
time: night
:::

Вороны исчезают в тёмном небе. Возле Ерсіна сидит сапсан. У когтей птицы тускло поблёскивает мониста.

:::dialogue
speaker: aibike
:::
А мониста всё-таки здесь. Мы до ночи за ней гнались…
:::

Қарашаш проводит ладонью по рукаву, счищая иней.

:::dialogue
speaker: karashash
:::
Я тоже за ней скакала. А теперь взгляни на рукав.
:::

:::ai_insert
id: yersin-warning-dialogue
type: dialogue
character: yersin
optional: true
max-chars: 200
:::
Звери уходят с привычных мест. Холод я замечал ещё до нападения.
:::

:::dialogue
speaker: aibike
:::
Зима уже идёт. Мы за этой монистой ничего не замечали.
:::

:::dialogue
speaker: karashash
:::
В аулах должны узнать про этот холод.
:::

:::choice
id: continue_together
icon: agree
goto: first-alliance
:::
Предложить продолжить путь вместе
:::

# Первый союз {#first-alliance}

:::scene
mood: mystery
time: night
:::

:::dialogue
speaker: aibike
:::
Ерсін, пойдём с нами. Расскажешь, что видел.
:::

:::dialogue
speaker: yersin
:::
Пойду.
:::

Айбике ещё раз смотрит на монисту, но руки к ней не тянет.

:::dialogue
speaker: karashash
:::
О ней потом договорим. Сейчас надо выбраться из холода.
:::

С поля боя уходят втроём.

:::memory
event: first-alliance-formed
:::

:::effect
set-flag: chapter-03-complete
set-flag: first-alliance-formed
set-variable: monisto-status=with-falcon
:::
