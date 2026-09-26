---
chapter-id: chapter-02
story-version: 0.2
language: ru
start: pursuit-continues
title: По следу корсака
---

# Погоня продолжается {#pursuit-continues}

:::scene
mood: tension
time: day
:::

Впереди мелькает рыжий хвост. Корсак бежит сквозь ковыль; при каждом скачке мониста звякает у него в зубах.

:::ai_insert
id: aibike-pursuit-dialogue
type: dialogue
character: aibike
optional: true
max-chars: 160
:::
Вон он, у гряды! Пока звенит, не потеряем.
:::

:::ai_insert
id: karashash-pursuit-dialogue
type: dialogue
character: karashash
optional: true
max-chars: 160
:::
А по сторонам ты смотришь? В этой траве ничего не видно. Держись рядом.
:::

:::choice
id: keep_corsac_in_sight
icon: leave
goto: wolves-across-path
:::
Не выпускать корсака из виду
:::

:::choice
id: move_together
icon: agree
goto: wolves-across-path
:::
Держаться рядом
:::

# Волки наперерез {#wolves-across-path}

:::scene
mood: danger
time: day
:::

Наперерез всадницам из ковыля выходят волки. Корсака они пропускают. Стая растягивается полукругом поперёк пути.

:::dialogue
speaker: karashash
:::
Справа двое. Не дай им зайти за спину.
:::

:::choice
id: use_bow
icon: attack
goto: ranged-clash
:::
Встретить стаю стрелами
:::

:::choice
id: hold_ground
icon: agree
goto: close-clash
:::
Удерживать позицию вместе
:::

# На расстоянии {#ranged-clash}

:::scene
mood: tension
time: day
:::

От первой стрелы вожак сворачивает. Айбике выбирает следующую цель. Қарашаш сдерживает остальных волков, не подпуская их к ней.

:::effect
set-variable: wolf-tactic=ranged
:::

:::check
stat: dexterity
difficulty: 7
success: falcon-strike
failure: wolves-close-in
:::

# Удержать круг {#close-clash}

:::scene
mood: danger
time: day
:::

Волки бросаются с двух сторон. Айбике и Қарашаш разворачивают коней навстречу друг другу. Стая напирает, но разделить всадниц ей не удаётся.

:::effect
set-variable: wolf-tactic=cooperative
:::

:::choice
id: break_wolf_circle
icon: attack
goto: falcon-strike
:::
Разорвать окружение
:::

# Стая приблизилась {#wolves-close-in}

:::scene
mood: danger
time: evening
:::

Один волк прорывается к всадницам. Қарашаш принимает удар на себя, давая Айбике время для точного выстрела.

:::effect
set-flag: difficult-wolf-fight
:::

:::choice
id: recover_position
icon: agree
goto: falcon-strike
:::
Снова встать рядом
:::

# Удар с неба {#falcon-strike}

:::scene
mood: mystery
time: evening
:::

Над схваткой проносится сапсан и почти отвесно падает на корсака. Зверёк уворачивается, выпустив цепочку из зубов.

Сапсан подхватывает монисту и взмывает вверх. Корсак скрывается в траве.

:::effect
set-flag: monisto-with-falcon
set-variable: monisto-carrier=falcon
:::

:::memory
event: falcon-took-monisto
:::

:::choice
id: finish_wolf_fight
icon: attack
goto: wolves-retreat
:::
Закончить бой с волками
:::

# Стая отступает {#wolves-retreat}

:::scene
mood: relief
time: evening
:::

Последний волк отступает в ковыль. Кони тяжело дышат. Вдалеке кричит сапсан.

:::memory
event: heroines-fought-wolves
:::

:::ai_insert
id: aibike-after-battle-dialogue
type: dialogue
character: aibike
optional: true
max-chars: 160
:::
Видишь? Мониста у птицы!
:::

:::ai_insert
id: karashash-after-battle-dialogue
type: dialogue
character: karashash
optional: true
max-chars: 160
:::
Не упусти птицу. Посмотрим, куда она летит.
:::

:::choice
id: follow_falcon
icon: leave
goto: glimmer-in-sky
:::
Определить направление полёта
:::

# Блеск в небе {#glimmer-in-sky}

:::scene
mood: mystery
time: evening
:::

В косом свете над степью вспыхивает знакомый блеск. Сапсан несёт монисту к далёкой возвышенности.

Айбике и Қарашаш направляют коней следом.

:::effect
set-flag: chapter-02-complete
set-variable: next-episode=icy-wings
set-variable: falcon-direction=high-ground
:::
