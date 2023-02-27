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

Додай код до функції `draw()`, щоб намалювати обличчя або маску. Не забудь видалити `pass` із середини функції.

У цьому прикладі коло намальоване в центрі, але ти можеш обрати іншу фігуру.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 11
line_highlights: 12
---

def draw():   
  ellipse(width/2, height/2, 200, 200) #Коло в центрі

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
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 11
line_highlights: 13
---

def draw():
  stroke(0) #Також можна використати no_stroke() 
  fill(255, 255, 0) #Яскраво-жовтий
  ellipse(width/2, height/2, 200, 200) #Коло в центрі

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Тест:** Запускай свій проєкт та змінюй колір до тих пір, поки не знайдеш бажаний результат.

--- /task ---

--- save ---
