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

Айбике и Қарашаш идут вслед за редкими вспышками монисты. Тени становятся длиннее, а осенний ветер приносит непривычный холод.

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

На вершине стоит незнакомый охотник. Сапсан опускается рядом с ним, всё ещё удерживая монисту. Айбике требует вернуть находку, а Қарашаш внимательно следит за руками незнакомца.

:::memory
event: heroines-met-yersin
:::

:::ai_insert
id: yersin-first-dialogue
type: dialogue
character: yersin
optional: true
max-chars: 180
:::
Я Ерсін. Птица принесла украшение сама, но сейчас опаснее то, от чего она сюда ушла.
:::

:::choice
id: ask_about_danger
icon: talk
goto: pale-movement
:::
Спросить об опасности
:::

:::choice
id: demand_monisto
icon: refuse
goto: pale-movement
:::
Снова потребовать монисту
:::

# Бледное движение {#pale-movement}

:::scene
mood: danger
time: evening
:::

Ответ прерывает шелест со всех сторон. Из сумеречного ковыля выходят корсаки, похожие на бледные отражения настоящих зверей. Они движутся слишком согласованно и окружают возвышенность.

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
Это не обычная стая. Держитесь вместе и не преследуйте тех, что уходят в дымку.
:::

:::choice
id: form_shared_line
icon: agree
goto: ghost-pack
:::
Удерживать общую позицию
:::

# Призрачная стая {#ghost-pack}

:::scene
mood: danger
time: evening
:::

Айбике бьёт издали, Қарашаш принимает первый натиск, а Ерсін замечает силуэты прежде, чем они выходят из дымки. Поодиночке каждый оказался бы окружён.

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
Под склон! На открытом месте холод настигнет раньше самих воронов.
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

Порыв холода останавливает прорыв. Призрачные корсаки снова сходятся, и героям приходится отступить к каменной стороне возвышенности.

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
К камням! Там ветер не сможет ударить с двух сторон.
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

Трое удерживают узкий проход. Стрелы рассеивают бледные силуэты, а Қарашаш не позволяет стае приблизиться. После последнего удара призрачные корсаки растворяются в сумраке.

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

Ледяные вороны заходят ещё раз. Герои выдерживают удар за камнями, и стая наконец поднимается выше.

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

Вороны исчезают в тёмном небе. Сапсан остаётся возле Ерсіна, а мониста тускло блестит рядом с его когтями.

:::ai_insert
id: yersin-warning-dialogue
type: dialogue
character: yersin
optional: true
max-chars: 200
:::
Я видел и другие признаки: звери покидают привычные места, а холод приходит раньше времени. Сегодня это уже нельзя считать случайностью.
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

Айбике, Қарашаш и Ерсін ещё не доверяют друг другу полностью. Но спор о монисте уступает место разговору об общей угрозе.

Трое впервые уходят с поля боя одной группой. Опасность больше не выглядит случайной встречей со степными хищниками.

:::memory
event: first-alliance-formed
:::

:::effect
set-flag: chapter-03-complete
set-flag: first-alliance-formed
set-variable: monisto-status=with-falcon
:::
