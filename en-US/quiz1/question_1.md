## Quick quiz

Answer the three questions. There are hints to guide you to the correct answer.

When you have answered each question, click on **Check my answer**.

Have fun!

--- question ---

---
legend: Question 1 of 3
---

In your project, you drew mouths using shapes.

What kind of mouth would this code draw?

--- code ---
---
language: python

---
def draw(): fill(0, 0, 0) #Black ellipse(160, 200, 150, 150) fill(255, 255, 255) #White ellipse(160, 150, 150, 150)

--- /code ---

--- choices ---

- ( ) ![](images/sad-mouth.png)

  --- feedback ---

  Not quite, to create a sad mouth the second `ellipse` would need a **y_coordinate** that is lower than the first `ellipse`.

  --- /feedback ---

- (x) ![](images/happy-mouth.png)

  --- feedback ---

  That's correct! The second `ellipse` is drawn with a **y_coordinate** that is higher than the first `ellipse`.

  --- /feedback ---

- () ![](images/circle-mouth.png)

  --- feedback ---

   Not quite, the second circle has a white `fill(255, 255, 255)` and is positioned partially over the first black circle.

  --- /feedback ---

- ( ) ![](images/square-mouth.png)

  --- feedback ---

The code does not draw rectangles. The `ellipse` function draws circles.

  --- /feedback ---

--- /choices ---

--- /question ---
