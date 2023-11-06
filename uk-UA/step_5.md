## Рот

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Рот - це чудовий спосіб вираження емоцій. Твій персонаж буде посміхатися, хмуритися або щось інше? 
</div>
<div>
![Зображення обличчя робота як приклад обличчя з ротом.](images/mask.png){:width="200px"}
</div>
</div>

--- task ---

Подумай, який рот потрібен твоєму обличчю. Найпростішим ротом може бути коло, щоб виглядати здивованим.

Ти можеш додати два кола, які накладаються один на одного, щоб створити посмішку або похмурість. Трикутники або прямокутники можуть бути використані для зубів.

--- /task ---

--- task ---

Додай код до своєї функції `draw()`, щоб додати рот.

--- collapse ---

---
title: Створи рот з накладених один на одного кругів
---

Встанови колір заливки `fill` для рота, потім намалюй овал `ellipse`. Знову встанови колір заливки `fill`, але який відповідає кольору обличчя. Потім намалюй другий овал `ellipse`.

Змінюй координату `y` другого овалу `ellipse` на трошки вищу позицію - для посмішки або на трошки нижчу - для похмурого обличчя.

![Область виводу із зображенням усміхненого рота.](images/smile.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # A black mouth
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0)  # An orange face
    ellipse(200, 235, 15, 15)  # Higher circle

--- /code ---

![Область виводу із зображенням похмурого рота.](images/frown.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0) #Чорний рот
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0) #Помаранчеве обличчя
    ellipse(200, 245, 15, 15) #Нижнє коло

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Створення рота за допомогою прямокутників
---

Роботи часто зображуються з ротами у формі прямокутника `rectangle`. Іноді, прямокутник `rectangle` та овал `ellipse` використовуються разом, щоб створити смайлик-кривляку або додати маску для обличчя.

![Область виводу показує обличчя з прямокутною маскою.](images/rectangle-mask.png)

Додай код для прямокутника `rectangle`, а потім створи всередині нього менший прямокутник `rectangle`. Змінюй кольори для `stroke` та `fill`, щоб доповнити тематику твого проєкту. Додай фігури овалів `ellipse`, якщо потрібно.

**Порада:** Не забувай розміщувати фігури овалів `ellipse` над кодом `rectangle`, якщо хочеш, щоб вони були позаду фігури прямокутника `rectangle`.

--- code ---
---
language: python
filename: main.py - draw()
---

    # Face mask
    no_fill()
    stroke(255, 255, 255)
    ellipse(150, 250, 30, 30)  # Left ear loop
    ellipse(250, 250, 30, 30)  # Right ear loop
    fill(255, 255, 255)
    no_stroke()
    rect(150, 230, 100, 40)  # Large white rectangle
    fill(108, 200, 206)
    rect(152, 235, 96, 30)  # Smaller blue rectangle

--- /code ---

--- /collapse ---

**Tip:** Add a `#Mouth` comment on the line before your mouth code to help you easily find the mouth code.

--- /task ---

--- task ---

**Choose:** You could also add multiple teeth to your mouth using `translate` to change the `x` coordinate after each tooth is drawn.

--- collapse ---

---
title: Додавання ряду зубів за допомогою петлі
---

Add code to create a `for` loop that repeats in order to create the number of teeth you need.

![The output area showing a robot face with a row of rectangle teeth in different colours.](images/robot-teeth.png)

After each tooth has been drawn, add code to `translate()` it by the width of the tooth.

Після того, як кожен зуб буде намальовано, додай код `translate()`, щоб зробити переведення зуба відповідно до його ширини.

--- code ---
---
language: python
filename: main.py - draw()
---

    # Mouth
    fill(90, 110, 184)
    red = 90  # Starting amount of red
    green = 110  # Starting amount of green
    blue = 180  # Starting amount of blue
    for i in range (0,6):
        rect(100, 300, 33, 50)
        fill(red, green, blue)  # Uses variables to control the colour change each loop
        red = red+40
        blue = blue-30
        translate(33, 0)  # Move along the x coordinate by the width of a tooth


--- /code ---

--- /collapse ---

[[[processing-translation]]]

--- collapse ---

---
title: Використовуй трикутники, щоб зобразити ікла
---

Create a `rectangle` to use as the line of the mouth.

Add two `triangle` shapes to create the fangs. Change the `x` coordinates for each corner to position the fangs at opposite ends of the mouth line.

![The output area showing a vampire face with a rectangle mouth and two triangle teeth.](images/vampire.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    # Mouth
    fill(0)
    rect(170, 260, 60, 5)  # Mouth line
    fill(0)
    triangle(170, 260, 180, 280, 190, 260)  # Left tooth
    triangle(210, 260, 220, 280, 230, 260)  # Right tooth
--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
title: Одна з накладених форм виходить за межі обличчя
---

If you use two overlapping shapes to create a mouth, then you need to make sure the shape that is the same colour as the face doesn't go outside the face. If it does, then change the width or height of the shape so that it's small enough to fit inside the face.

--- /collapse ---


--- collapse ---

---
title: Занадто багато зубів
---

Don't forget that `range()` creates a sequence of numbers starting from 0 not 1. This may make a difference to your code depending on how you have positioned your teeth.

--- /collapse ---

--- /task ---

--- save ---
