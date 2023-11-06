## Очі

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Додавши очі, твоя фігура вже буде схожа на обличчя.
</div>
<div>
![Область виводу, яка показує обличчя з очима.](images/eyes.png){:width="200px"}
</div>
</div>

--- task ---

Подумай над тим, які очі підійдуть до твого обличчя. Найпростіший варіант очей – це 2 кола.

Можна додавати різнокольорові райдужки та зіниці. Можна додати світлові відблиски / підсвічування різного кольору.

--- /task ---

Експериментуй з фігурами `ellipses` у функції `draw`, щоб отримати ті очі, які тобі сподобаються.

--- task ---

### Позиціонування очей

Перше число у `ellipse` - це центр ока. Очі повинні бути розташовані на однаковій відстані від центру малюнка.

У цьому прикладі, `160` та `240` знаходяться на відстані `40` пікселів із 200, що підходить для малюнка шириною 400.

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Black — change to red, green, or blue up to 255
    eye_size = 50
    ellipse(160, 180, eye_size, eye_size)  # x, y, width, height
    ellipse(240, 180, eye_size, eye_size)

--- /code ---

**Tip:** If you want round eyes, then using an `eye_size` variable makes it easier to change the width and height of both eyes in one place.

[[[processing-python-ellipse]]]

--- collapse ---

---
title: Визначення позицій за допомогою ширини
---

The centre of a drawing is at position `width / 2` or half the width. You can use this to position the eyes by subtracting the eye width for the left eye and adding it for the right eye:

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Black — change to red, green, or blue up to 255
    eye_size = 50
    ellipse( (width / 2) - 40, 180, eye_size, eye_size)  # x, y, width, height
    ellipse( (width / 2) + 40 , 180, eye_size, eye_size)

--- /code ---

fill(0, 0, 0) #Чорний; можна змінити на червоний, зелений або синій до 255 eye_size = 50 ellipse( (width / 2) - 40, 180, eye_size, eye_size) #x, y, ширина, висота ellipse( (width / 2) + 40 , 180, eye_size, eye_size)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Black — change to red, green, or blue up to 255
    ellipse( (width / 2) - (width / 10) , 180, eye_size, eye_size)  # x, y, width, height
    ellipse( (width / 2) + (width / 10) , 180, eye_size, eye_size)

--- /code ---

--- /collapse ---

fill(0, 0, 0) #Чорний; можна змінити на червоний, зелений або синій до 255 ellipse( (width / 2) - (width / 10) , 180, eye_size, eye_size) #x, y, ширина, висота ellipse( (width / 2) + (width / 10) , 180, eye_size, eye_size)

--- /task ---

--- task ---

Заміни друге число у функції `ellipse`, щоб перемістити `y` - (вертикальне) розташування очей.

**Tip:** If you set a stroke for drawing the face and don't want one for the eyes, then you will need to call `no_stroke()` before drawing the eyes.

[[[processing-stroke]]]

--- /task ---

--- task ---

### Додавання деталей

You can use more circles to create:
+ Кольорові райдужки
+ Чорні зіниці
+ Білі світлові відблиски
+ Або щось інше

This eye has a coloured iris, black pupil, and white catchlights with changed opacity: ![The output area showing an eye with catchlights over the pupil and iris.](images/catchlights.png)

\[[[generic-theory-simple-colours]]\] \[[[processing-opacity\]]]

Ти можеш використовувати більше кружечків, щоб створювати:

[[[processing-rotation]]]

--- /task ---

--- task ---

**Test:** Keep changing the eyes until you like the way they look.

Is your drawing starting to look like a face?

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: Очі не знаходяться в центрі
---

You could use `height / 2` to place them in the centre.

--- /collapse ---

--- collapse ---
---
title: Очі не розташовані на одному рівні
---

If you want the eyes to be aligned, then make sure you use the same number for the coordinates for both eyes. Try using a variable so that the values are always the same.

--- /collapse ---

--- collapse ---

---
title: Зіницю або райдужну оболонку не видно
---

The eye needs to be drawn first, then the iris, and finally the pupil. The order in which you draw things is very important.

Computer graphics are made of layers. In your eye, each ellipse is a layer. Objects on higher layers sit in front of objects on lower layers. Imagine cutting all the shapes out of paper. Depending on how you arrange and overlap that paper, the final result could look very different.

--- /collapse ---

--- collapse ---

---
title: Очі не круглі
---

The third and fourth numbers in `ellipse` are the width and height of the eyes.

**Tip:** If you make them the same, you will get round eyes.

--- /collapse ---


--- /task ---

--- save ---
