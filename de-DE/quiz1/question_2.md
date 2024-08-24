--- question ---

---
legend: Frage 2 von 3
---

In your project, you added code to draw a face with many features. Die Reihenfolge deines Codes war äußerst wichtig, damit dein Gesicht wie dein Design aussieht.

Wenn du diesen Code ausführen würdest, wie würde das Gesicht aussehen?

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

![Ein weißes Gesicht mit schwarzer Umrandung. Es gibt zwei grüne Augen mit schwarzen Umrandungen.](images/face1.png)

 --- feedback ---

 Nicht ganz, achte auf die Reihenfolge der `ellipse()` und `stroke()` Funktionen.

 --- /feedback ---

- ( )

![Ein weißes Gesicht mit schwarzer Umrandung. There are two green eyes with black pupils and both have a black outline.](images/face2.png)

 --- feedback ---

 Nicht ganz, achte auf die Reihenfolge der `stroke()` Funktionen.

 --- /feedback ---

- (x)

![Ein weißes Gesicht mit schwarzer Umrandung. There are two green eyes with black pupils and the eyes do not have an outline.](images/face3.png)

 --- feedback ---

 Correct, the code draws a face with a black stroke then turns off the stroke before drawing the circles. The green circles are drawn first with the black circles on top of them.

 --- /feedback ---

- ( )

![A white face with black outline. Es gibt zwei grüne Augen, die keine Umrandung haben.](images/face4.png)

 --- feedback ---

 Not quite, look at the order of the `ellipse()` functions.

 --- /feedback ---

--- /choices ---

--- /question ---
