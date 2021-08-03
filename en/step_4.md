## Add eyes

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Eyes make a shape start to look like a face.
</div>
<div>
![The output area showing a face with eyes.](images/eyes.png){:width="200px"}
</div>
</div>

--- task ---
Think about what kind of eyes your face needs. The simplest eyes are just two circles. 

You could add different coloured irises and pupils. You could add light highlights in a different colour. 

--- /task ---

--- task ---
Add code to your `draw` function to add two eyes.

This example will draw two round black eyes:

--- code ---
---
language: python
filename: main.py - draw()
---

  fill(0, 0, 0) # black - change to red, green, blue up to 255
  ellipse(160, 220, 50, 50) # x, y, width, height
  ellipse(240, 220, 50, 50)

--- /code ---

--- /task ---

You can change the change the colour and position of the eyes to get the result you want.

[[[processing-python-ellipse]]]

[[[generic-theory-simple-colours]]]

--- task ---
**Test:** Run your project each time you change it so you can see the progress you've made.
--- /task ---

--- task ---
Position the eyes to suit the face you are drawing. 

The first number in `ellipse` is the center of the eye. The eyes should be the same distance from the center of the drawing. 

In the example, `160` and `240` are both '40' pixels away from 200 which works for a drawing with a width of 400. You will need different numbers if your drawing has a different width. 

You can either change the numbers or calculate the values.

--- collapse ---

---
title: Calculating positions based on width
---

The centre of a drawing is at position `width / 2` or half the width. You can use this to position the eyes by subtracting the eye width for the left eye and adding it for the right eye:

--- code ---
---
language: python
filename: main.py - draw()
---

  fill(0, 0, 0) # black - change to red, green, blue up to 255
  ellipse( (width / 2) - 40, 220, 50, 50) # x, y, width, height
  ellipse( (width / 2) + 40 , 220, 50, 50)

--- /code ---

You could also calculate the width of the eyes based on width of the drawing.

--- code ---
---
language: python
filename: main.py - draw()
---

  fill(0, 0, 0) # black - change to red, green, blue up to 255
  ellipse( (width / 2) - (width / 10) , 220, 50, 50) # x, y, width, height
  ellipse( (width / 2) + (width / 10) , 220, 50, 50)

--- /code ---

--- /collapse ---

--- /task ---

--- task ---
You can also change the second number in the `ellipse` function call to change the y (vertical) position of the eyes. 

You could use `height / 2` to place them in the centre.

If you want the eyes to be aligned then make sure you use the same number in for both eyes.

--- /task ---

--- task ---

The third and fourth numbers in `ellipse` are the width and height of the eyes. If you make them the same you will get round eyes.

Experiment until you are happy with the eyes. 

--- /task ---

--- task ---
You can use more circles to create pupils or coloured irises.

You could also add white highlights to create a cute effect like in the Kawaii fruit example.
--- /task ---

--- task ---
**Test:** Keep changing the eyes until you like the way they look.

Is your drawing starting to look like a face?
--- /task ---

--- save ---