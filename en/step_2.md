## Choose a background colour

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Have you got an idea about the kind of face or mask you want to make? Use this step to plan your art and set up your canvas.
</div>
<div>
![The output area with a vampire-themed face.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Open the [starter project](https://editor.raspberrypi.org/en/projects/make-face-starter){:target="_blank"}. 

--- /task ---

--- task ---
The three numbers in `background(0, 0, 0)` are red, green and blue values. Experiment with changing the numbers to any whole number between 0 and 255 to change the background colour. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 12
---
 
def draw():   
    # Put code to run every frame here
    background(0, 0, 0)    
  
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and you should see a coloured square. 

--- /task ---
