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

You could add different coloured irises and pupils. You could add light highlights / catchlights in a different colour. 

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

Experiment with ellipses to create the eyes you want. Here are some tips to help:

**Tip:** The first number in `ellipse` is the center of the eye. The eyes should be positioned the same distance from the centre of the drawing. In the example, `160` and `240` are both '40' pixels away from 200 which works for a drawing with a width of 400.  

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

Change the second number in the `ellipse` function call to move the y (vertical) position of the eyes. 

**Tip:** You could use `height / 2` to place them in the centre.

**Tip:** If you want the eyes to be aligned then make sure you use the same number in for both eyes.

--- /task ---

--- task ---

The third and fourth numbers in `ellipse` are the width and height of the eyes. 

**Tip:** If you make them the same you will get round eyes.

--- /task ---

--- task ---

**Test:** Keep changing the eyes until you like the way they look.

Is your drawing starting to look like a face? 

**Tip:** You can use more circles to create pupils or coloured irises.

--- /task ---

--- save ---