## Add a mouth

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
A mouth is a great way of showing emotion. Will your character have a smile, frown or something else? 
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Think about what kind of mouth your face needs. The simplest mouth would be a circle to look surprised. 

You could add two overlapping circles to create a smile or frown. Triangles or rectangles could be added for teeth. 

--- /task ---

--- task ---

Add code to your `draw()` function to add a mouth.

--- collapse ---

---
title: create a mouth from overlapping circles
---

Set the `fill` colour for your mouth then draw a `ellipse`. Set the `fill` colour to match the face colour then draw a second `ellipse` with a slightly higher `y-coordinate` to make a smile or a slightly lower `y-coordinate` to make a frown. 

![The output area showing a smiling mouth](images/smile.png)

--- code ---
---
language: python
filename: main.py
---

    fill(0, 0, 0) # a black mouth
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0) # an orange face
    ellipse(200, 235, 15, 15) # higher circle

--- /code ---

![The output area showing a frowning mouth](images/frown.png)

--- code ---
---
language: python
filename: main.py
---

    fill(0, 0, 0) # a black mouth
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0) # an orange face
    ellipse(200, 245, 15, 15) # lower circle

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Create a mouth using rectangles
---



--- /collapse ---

**Tip:** add a `# Mouth` comment on the line before your mouth code to help you easily find the mouth code.

--- /task ---

--- task ---

**Choose:** You could also add teeth to your mouth using shapes that change their `x-coordinate`. 

--- collapse ---

---
title: Use a loop to add a row of teeth
---

![The output area showing a robot face with a row of rectangle teeth in different colours.](images/robot-teeth.png)

--- code ---
---
language: python
filename: main.py
---

# Mouth
  fill(90, 110, 184) # starter fill colour
  red = 90 # starting amount of red
  green = 110 # starting amount of green
  blue = 180 # starting amount of blue
  gap = 0 # starting amount of gap
  for i in range (0,6): # creates a row of teeth 
    rect(100+gap, 300, 33, 50) # x-coordinate uses gap variable to move it each loop
    gap = gap+33 # increases each loop
    fill(red, green, blue) # uses variables to control colour change each loop
    red = red+40 # increases each loop
    blue = blue-30 # increases each loop

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Use triangles to add fangs
---



--- /collapse ---

--- /task ---

--- save ---