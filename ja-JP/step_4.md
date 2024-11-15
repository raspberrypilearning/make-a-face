## Rectangles

Rectangles are drawn in almost the same way as an ellipse.

--- task ---

Change the function `ellipse` to instead call the function `rect`.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 17
---

def draw(): # Put code to run every frame here background(255, 255, 255)  
# Add code to draw your face here fill(255, 255, 0) rect( screen_size/2, screen_size/2, 100, 50 )

--- /code ---

--- /task ---

--- task --- **Test:** Run your code to see a rectangle instead of an ellipse.

--- /task ---

The first two values for `rectangle` and `ellipse` represent the x, y coordinates of the centre of the shape. At the moment they are set to `screen_size/2` to position the shape in the centre of the screen.

The top left corner of the screen is coordinate `0`,`0`. Increasing the `x` value will move the shape to the right. Increasing the `y` value will move the shape downwards.


--- task ---

Change the position values to alter where the shape appears on the screen.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 18-19
---

def draw(): # Put code to run every frame here background(255, 255, 255)  
# Add code to draw your face here fill(255, 255, 0) rect( 80, # x coordinate 60, # y coordinate 100, 50 )

--- /code --- --- /task ---

--- task ---

**Test:** Experiment with changing the coordinates, then run your code to see where the ellipse or rectangle is displayed.

--- /task ---