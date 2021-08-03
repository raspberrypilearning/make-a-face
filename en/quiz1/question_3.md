
--- question ---

---
legend: Question 3 of 3
---

In your project, you used functions to draw a face.

Here, you want to code a rectangle face shape. Which code would draw a rectangle? 

--- choices ---

- ( ) --- code ---
---
language: python
---

def setup():
  size(400, 400) # width and height
  background(255, 255, 255)
  fill(99, 43, 108)  
  rect(100, 100, 200, 200)

def draw():

run()

--- /code ---

  --- feedback ---

  This would not draw a rectangle because there is no code in the `draw` functions so the program would return an error. What would you move to the `draw` function?

  --- /feedback ---

- (x) --- code ---
---
language: python
---

def setup():
  size(400, 400) # width and height
  background(255, 255, 255)

def draw():
  fill(99, 43, 108)  
  rect(100, 100, 200, 200)

run()

--- /code ---


  --- feedback ---

  Yes, the code here is organised into two functions. The first `setup` function sets the size and background and the second `draw` function draws a filled rectangle.

  --- /feedback ---

- () --- code ---
---
language: python
---

def setup():

def draw():
  size(400, 400) # width and height
  background(255, 255, 255)
  fill(99, 43, 108)  
  rect(100, 100, 200, 200)

run()

--- /code ---


  --- feedback ---

  This code would not draw a rectangle, because the screen output `size` is not set in the `setup` function and having no code in the 'setup' function would cause the program to return an error. What would you move to the 'setup' function

  --- /feedback ---

- ( ) --- code ---
---
language: python
---

def setup():
  fill(99, 43, 108)  
  rect(100, 100, 200, 200)

def draw():
  size(400, 400) # width and height
  background(255, 255, 255)

run()

--- /code --- 

  --- feedback ---

  No, this would cause an error. Look at the functions again, `setup` is called when the project starts to set up the initial screen. `draw` is called after `setup` to draw the shapes.

  --- /feedback ---

--- /choices ---

--- /question ---
