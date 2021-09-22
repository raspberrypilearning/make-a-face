## Face shape

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Draw and colour a shape for your face or mask. Don't add the other features just yet, they will come later.
</div>
<div>
![Image of a square faced robot.](images/robot-teeth.png){:width="200px"}
</div>
</div>

--- task ---
Decide on the main shape of the face for your mask. It could be a circle, an ellipse, a rectangle, or even a triangle.

Add code to the `draw()` function to draw a face or mask. Make sure you also remove `pass` from inside the function.

This example draws a circle in the middle, but it's up to you which shape to use.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 11
line_highlights: 12
---
def draw():
  ellipse(width/2, height/2, 200, 200) # circle in the middle
--- /code ---

![The output area showing a black circle in the middle of the grid](images/black-circle.png)

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---
**Test:** Run your code and change it to get the face size and shape that you want.

--- /task ---

--- task ---

Choose a stroke colour for the outline and a fill colour for the main part of the shape.

[[[processing-stroke]]]

If you don't want an outline then use `no_stroke()`.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 11
line_highlights: 13
---
def draw():
  stroke(0) # you can also use no_stroke() 
  fill(255, 255, 0) # bright yellow
  ellipse(width/2, height/2, 200, 200) # circle in the middle
--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---
**Test:** Run your code and change the colour until you are happy with it.

--- /task ---

--- save ---