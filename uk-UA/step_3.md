## Форма обличчя

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Намалюй та пофарбуй фігуру для твого обличчя або маски. Поки що не додавай ніяких деталей, залиш це на потім.
</div>
<div>
![Квадратне обличчя робота.](images/robot-teeth.png){:width="200px"}
</div>
</div>

--- task ---

Визнач, якою буде основна фігура для твого обличчя або маски. Це може бути коло, овал, прямокутник, або навіть трикутник.

Add code to the `draw()` function to draw a face or mask.

У цьому прикладі коло намальоване в центрі, але ти можеш обрати іншу фігуру.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 10
line_highlights: 14, 15
---

def draw(): # Put code to run every frame here background(255, 255, 255)  # Change to your background colour

    # Add code to draw your face here
    ellipse(width/2, height/2, 200, 200)  # Circle in the middle
    
    grid()  # add a # to the beginning of this line to hide the grid

--- /code ---

![Область виводу коду показує чорне коло, розташоване в центрі.](images/black-circle.png)

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---

**Тест:** Запускай свій код та змінюй його, щоб отримати бажаний розмір та форму обличчя.

--- /task ---

--- task ---

Обери колір обведення для контуру та колір заливки для основної частини фігури.

[[[processing-stroke]]]

Якщо тобі не потрібен контур, використовуй функцію `no_stroke()`.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 11
line_highlights: 13
---

    # Add code to draw your face here
    fill(255, 255, 0)  # Bright yellow
    ellipse(width/2, height/2, 200, 200)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Run your code and change the colour until you are happy with it.

--- /task ---

--- save ---
