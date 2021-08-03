## Choose a theme

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Have you got an idea about the kind of face or mask you want to make? Use this step to plan your art and set up your canvas.
</div>
<div>
![The output area with a vampire themed face.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Open the [starter project](https://trinket.io/library/trinkets/21dc61a9de){:target="_blank"}. Trinket will open in another browser tab.

[[[python-offline]]]

--- /task ---

--- task ---

**Choose:** Think about the kind of face you want to make: 
+ Do you want to choose something from your heritage or popular culture? 
+ Will your art show a human, animal, something mythical or perhaps a machine? 
+ You might even want to create a self-portrait!  

--- /task ---

--- task ---

The first thing to do when creating art using the Python Processing library is to define a `setup` function that is run once at the beginning of your programme.

The starter project has a `setup` function that sets the `size` of your canvas to `480` width and `400` height. 

**Choose:** Experiment with the numbers and run your code to find a size that you are happy with:  

--- collapse ---

---
title: Setting the screen size when your programme starts
---

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 6
line_highlights: 7
---
def setup():
    size(480, 400) # 400, 400 works well for a round face

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Choose:** Think about the colours you will use for your face and change the `background` colour values to set your screen to a complementary colour:

[[[generic-theory-simple-colours]]]

--- collapse ---

---
title: Setting the background colour when your programme starts
---

--- code ---
---
language: python
filename: main.py - setup()
line_numbers: true
line_number_start: 9
line_highlights: 9
---
    background(255, 255, 255) # Try different numbers to change the colour 

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Tip:** The `setup` function has `grid()` code. This adds a coordinates grid over your background that helps work out where to position features on your face. 

To turn the grid off add a `#` in front of the code, to turn it back on remove the `#` 

--- code ---
---
language: python
filename: main.py - setup()
---
    grid() # Shows grid 

--- /code ---

--- code ---
---
language: python
filename: main.py - setup()
---
    # grid() # Hide grid by turning it into a comment 

--- /code ---

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
title: I've updated my size and colour but the output area stays the same
---

After changing the code, you will need to `run` your project to see the changes in the output area. 

--- /collapse ---

--- collapse ---

---
title: I've tried different numbers but the background color doesn't change 
---

The maximum amount of red, green or blue is `255`. Make sure all your `background` colour values are between `0` and `255`.  

--- /collapse ---

--- /task ---

--- save ---