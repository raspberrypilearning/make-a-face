--- question ---

---
legend: Pytanie 2 z 3
---

In your project, you added code to draw a face with many features. The order of your code was extremely important to make the face look like your design.

If you ran this code, what would the face look like?

--- code ---
---
language: python

---

def draw():

  #Face stroke(0) #Black fill(255) #White ellipse(200, 200, 200, 190) no_stroke()

  #Eyes fill(0, 255, 0) #Green ellipse(160, 180, 60, 60) ellipse(240, 180, 60, 60) fill(0) #Black ellipse(160, 180, 30, 30) ellipse(240, 180, 30, 30)

run()

--- /code ---

--- choices ---

- ( )

![A white face with black outline. There are two solid green eyes with black outlines.](images/face1.png)

 --- feedback ---

 Not quite, look at the order of the `ellipse()` and the `stroke()` functions.

 --- /feedback ---

- ( )

![A white face with black outline. There are two green eyes with black pupils and both have a black outline.](images/face2.png)

 --- feedback ---

 Not quite, look at the order of the `stroke()` functions.

 --- /feedback ---

- (x)

![A white face with black outline. There are two green eyes with black pupils and the eyes do not have an outline.](images/face3.png)

 --- feedback ---

 Correct, the code draws a face with a black stroke then turns off the stroke before drawing the circles. The green circles are drawn first with the black circles on top of them.

 --- /feedback ---

- ( )

![A white face with black outline. There are two solid green eyes that do not have an outline.](images/face4.png)

 --- feedback ---

 Not quite, look at the order of the `ellipse()` functions.

 --- /feedback ---

--- /choices ---

--- /question ---
