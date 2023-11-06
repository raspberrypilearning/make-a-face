## Adicione olhos

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Os olhos fazem uma forma começar a se parecer com um rosto.
</div>
<div>
![A área de saída mostrando um rosto com olhos.](images/eyes.png){:width="200px"}
</div>
</div>

--- task ---

Pense em que tipo de olhos seu rosto precisa. Os olhos mais simples são apenas dois círculos.

Você pode adicionar íris e pupilas de cores diferentes. Você pode adicionar realces de luz / holofotes em uma cor diferente.

--- /task ---

Experimente com `elipses` na função `draw` para criar os olhos que você deseja.

--- task ---

### Posicione os olhos

O primeiro número na função `ellipse` é o centro do olho. Os olhos devem estar posicionados à mesma distância do centro do desenho.

Neste exemplo, `160` e `240` estão ambos `40` píxeis de distância de 200, o que funciona para um desenho com uma largura de 400.

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
title: Calculando posições com base na largura
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

You could also calculate the width of the eyes based on the width of the drawing.

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

Change the second number in the `ellipse` function call to move the `y` (vertical) position of the eyes.

--- /task ---

--- task ---

**Test:** Keep changing the shape and position of the eyes until you like the way they look.

**Tip:** If you set a stroke for drawing the face and don't want one for the eyes, then you will need to call `no_stroke()` before drawing the eyes.

[[[processing-stroke]]]

--- /task ---

--- task ---

### Adicione detalhes

You can use more circles to create:
+ Íris coloridas
+ Pupilas negras
+ Holofotes brancos
+ Ou alguma outra coisa

This eye has a coloured iris, black pupil, and white catchlights with changed opacity: ![The output area showing an eye with catchlights over the pupil and iris.](images/catchlights.png)

\[[[generic-theory-simple-colours]]\] \[[[processing-opacity\]]]

You can also animate the eyes by rotating them.

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
título: Os olhos não estão centrados
---

You could use `height / 2` to place them in the centre.

--- /collapse ---

--- collapse ---
---
título: Os olhos não estão alinhados entre si
---

If you want the eyes to be aligned, then make sure you use the same number for the coordinates for both eyes. Try using a variable so that the values are always the same.

--- /collapse ---

--- collapse ---

---
título: Não consigo ver a pupila ou a íris
---

The eye needs to be drawn first, then the iris, and finally the pupil. The order in which you draw things is very important.

Computer graphics are made of layers. In your eye, each ellipse is a layer. Objects on higher layers sit in front of objects on lower layers. Imagine cutting all the shapes out of paper. Depending on how you arrange and overlap that paper, the final result could look very different.

--- /collapse ---

--- collapse ---

---
título: Meus olhos não são redondos
---

The third and fourth numbers in `ellipse` are the width and height of the eyes.

**Tip:** If you make them the same, you will get round eyes.

--- /collapse ---


--- /task ---

--- save ---
