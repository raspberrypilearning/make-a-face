## Overlap shapes

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
A mouth is a great way of showing emotion. Will your character have a smile, frown, or something else? 
</div>
<div>
![Image showing a robot face as an example of a face with a mouth.](images/mask.png){:width="200px"}
</div>
</div>

You can make shapes you couldn't otherwise create by overlapping shapes, for example yu could add two overlapping circles to create a smile. 

--- task ---

Start with an ellipse to represent the face. 


--- code ---
---
language: python
line_numbers: true
line_number_start: 11
line_highlights: 15-16
---
def draw():
    # Put code to run every frame here
    background(125, 0, 125)
    # Add code to draw your face here
    fill(125, 75, 0) # Brown
    ellipse(200, 220, 150, 150) # Face
--- /code ---

--- /task ---

--- task ---

Set the `fill` colour for your mouth then draw an `ellipse`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 18-21
---
def draw():
    # Put code to run every frame here
    background(125, 0, 125)
    # Add code to draw your face here
    fill(125, 75, 0) # Brown
    ellipse(200, 220, 150, 150) # Face
    fill(255, 0, 0)  # Red
    ellipse(200, 240, 40, 40) # Mouth

--- /code ---

--- /task ---

--- task ---
Set the `fill` colour to match the face colour, then draw a second `ellipse`.

Change the `y` coordinate of the second `ellipse` to a slightly higher position for a smile.


--- code ---
---
language: python
line_numbers: true
line_number_start: 18
line_highlights: 20-21
---
    fill(255, 0, 0)  # Red
    ellipse(200, 240, 40, 40) # Mouth
    fill(125, 75, 0) # Brown
    ellipse(200, 235, 40, 40) # Overlap   

--- /code ---

--- /task ---

--- task ---
**Test:** Experiment with changing the fill colours and sizes of the ellipses. Run your program to see the results.
--- /task ---