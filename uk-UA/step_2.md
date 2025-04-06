## Вибери колір тла

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ти вже маєш уявлення про те, яке обличчя або маску хочеш створити? На цьому етапі ти можеш спланувати свою роботу та підготувати своє полотно.
</div>
<div>
![Область виводу з обличчям-вампіром.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Відкрий [початковий проєкт](https://editor.raspberrypi.org/en/projects/make-face-starter){:target="_blank"}.

--- /task ---

--- task ---

Три числа у функції тла ` background(0, 0, 0)` — це значення червоного, зеленого та синього кольорів. Поекспериментуй з різними цілими числами від 0 до 255 і зміни колір тла.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 14
---

def draw():   
# Put code to run every frame here background(0, 0, 0)

--- /code ---

--- /task ---

--- task ---

**Протестуй:** запусти свій код. Ти побачиш своє тло у вигляді зафарбованого квадрата.

--- /task ---
