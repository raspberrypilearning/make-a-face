## Face shape

Draw and colour a shape for your face or mask. 

An **ellipse** is an oval shape. If you specify the same width and height, you will draw a circle.  

--- task ---

Add code to the `draw()` function to set the fill colour in the same way as before using red, green and blue values. 
Then, draw a circle in this colour.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 14-20
---

def draw():
    # Put code to run every frame here
    background(255, 255, 255)  
    # Add code to draw your face here
    fill(255, 255, 0) 
    ellipse(
        screen_size/2, 
        screen_size/2, 
        200, 
        200
    )  
  
--- /code ---

--- /task ---

--- task ---
**Test:** Run your code and you should see a coloured circle. Make sure that the fill colour of your ellipse is not the same colour as your background!

--- /task ---

--- task ---

Change the width and height values to see the ellipse change shape. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 18-19
---

def draw():
    # Put code to run every frame here
    background(255, 255, 255)  
    # Add code to draw your face here
    fill(255, 255, 0) 
    ellipse(
        screen_size/2, 
        screen_size/2, 
        100, 
        50
    )  
  
--- /code ---

--- /task ---

--- task ---

Before the code where you draw the ellipse, you can choose to set a colour and thickness. Or, if you prefer, you can remove the stroke and have no outline.


--- code ---
---
language: python
line_numbers: true
line_number_start: 14
line_highlights: 15-16
---
    fill(255, 255, 0) 
    stroke(255, 255, 255)  
    stroke_weight(3)
    ellipse(
        screen_size/2, 
        screen_size/2, 
        100, 
        50
    )  
    
--- /code ---

--- code ---
---
language: python
line_numbers: true
line_number_start: 14
line_highlights: 15
---
    fill(255, 255, 0) 
    no_stroke()
    ellipse(
        screen_size/2, 
        screen_size/2, 
        100, 
        50
    )  
  
--- /code ---

--- /task ---

--- task ---
**Test:** Experiment with changing the stroke colour and thickness or removing it, then run your code to see the results. 
--- /task ---