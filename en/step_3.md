## Face shape

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Draw and colour a shape for your face or mask.
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

--- task ---
Decide on the main shape of the face for your mask. It could be a circle, an ellipse, a rectangle, or even a triangle.

Add code to the `draw` function to draw a face or mask. 

This example uses a circle, but it's up to you.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11
line_highlights: 12
---
def draw():
  ellipse(width/2, height/2, 200, 200) # circle in the middle
--- /code ---

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---
**Test:** Run your code and change it to get the face size and shape that you want.

--- /task ---

--- task ---

Choose a stroke colour for the outline and a fill colour for the main part of the shape.

If you don't want an outline then use `no_stroke()`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 11
line_highlights: 13
---
def draw():
  stroke(0) # you can also use no_stroke() 
  fill(255, 255, 0) # bright yellow
  ellipse(width/2, height/2, 200, 200) # circle in the middle
--- /code ---


[[processing-rgb-colours]]

--- /task ---

--- task ---
**Test:** Run your code and change the colour until you are happy with it.

--- /task ---

--- save ---