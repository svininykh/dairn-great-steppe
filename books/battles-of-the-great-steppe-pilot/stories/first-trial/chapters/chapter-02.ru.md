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

Осенний день клонится к вечеру. Впереди снова мелькает корсак, а мониста позвякивает в его зубах.

:::ai_insert
id: aibike-pursuit-dialogue
type: dialogue
character: aibike
optional: true
max-chars: 160
:::
След свежий. Если не потеряем его у гряды, он нас не обманет.
:::

:::ai_insert
id: karashash-pursuit-dialogue
type: dialogue
character: karashash
optional: true
max-chars: 160
:::
Смотри не только вперёд. В высокой траве слишком легко попасть в засаду.
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

Из ковыля выходят волки. Они не преследуют корсака: стая расходится полукругом и отрезает всадницам путь.

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

Первая стрела заставляет вожака свернуть. Қарашаш не позволяет остальным приблизиться, пока Айбике выбирает следующую цель.

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

Волки бросаются с двух сторон. Героини разворачивают коней навстречу друг другу и не дают стае разделить их.

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

Один из волков прорывается слишком близко. Қарашаш принимает удар на себя, а Айбике получает время для точного выстрела.

:::effect
set-flag: difficult-wolf-fight
:::

:::choice
id: recover_position
icon: agree
goto: falcon-strike
:::
Восстановить общую позицию
:::

# Удар с неба {#falcon-strike}

:::scene
mood: mystery
time: evening
:::

Пока продолжается бой, над степью проносится сапсан. Он падает на корсака почти отвесно. Зверёк успевает уклониться, но выпускает монисту.

Птица подхватывает украшение как единственную добычу и взмывает в небо. Корсак скрывается в траве уже без него.

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

Последний волк отступает в ковыль. Над полем боя остаются только тяжёлое дыхание коней и удаляющийся крик сапсана.

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
Мы потеряли корсака, но мониста всё ещё показывает нам путь.
:::

:::ai_insert
id: karashash-after-battle-dialogue
type: dialogue
character: karashash
optional: true
max-chars: 160
:::
Птица летит к возвышенности. Там и узнаем, куда она несёт находку.
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

Айбике и Қарашаш снова отправляются в путь. Корсак спасся, но погоня получила новое направление.

:::effect
set-flag: chapter-02-complete
set-variable: next-episode=icy-wings
set-variable: falcon-direction=high-ground
:::
