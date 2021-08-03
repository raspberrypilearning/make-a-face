
--- question ---

---
legend: Question 2 of 3
---

In the project you added two eyes and used the **y-coordinate** to veritically align them. The code below draws a face but the eyes are not vertically aligned. 

--- code ---
---
language: python
---

def draw():
  fill(99, 43, 108)  
  rect(100, 100, 200, 200) # Face
  fill(240,159,156)
  ellipse(150, 150, 60, 80) # Left eye
  ellipse(250, 200, 60, 80) # Right eye
  fill(199,107,152)
  rect(150, 250, 100, 30) # Mouth

Which value in your right-eye `ellipse` function would need to be changed to verically aligned both eyes. 

--- /code ---

![Image with a rectangle face and mouth and two ellipse eyes. The eyes are not veritcally aligned as the right eye is lower on the screen than the left.](images/lobsided-eyes.png)

--- choices ---

- ( ) `60`

  --- feedback ---

  No, this controls the width of the `ellipse`. Both eyes have the same width. 

  --- /feedback ---

- ( ) `80`

  --- feedback ---

  No, this controls the height of the `ellipse`. Both eyes have the same height. 

  --- /feedback ---

- () `250`

  --- feedback ---

  Not quite, `250` is the **x-coordinate** in an `ellipse` and controls the horizontal position. If this value was changed the eyes would not be positioned equally along the horizontal axis.

  --- /feedback ---

- (x) `200`

  --- feedback ---

  That's correct! `200` is the **y-coordinate** in an `ellipse`. To make both `ellipse(x-coordinate, y-coordinate, width, height)` vertically align the right-eye ellipse must be `ellipse(250, 150, 60, 80)`   

  --- /feedback ---

--- /choices ---

--- /question ---
