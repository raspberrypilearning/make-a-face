--- question ---

---
legend: Frage 2 von 3
---

In deinem Projekt hast du Code geschrieben, um ein Gesicht mit vielen Merkmalen zu zeichnen. Die Reihenfolge deines Codes war äußerst wichtig, damit dein Gesicht wie dein Design aussieht.

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

![Ein weißes Gesicht mit schwarzer Umrandung. Da sind zwei grüne Augen mit schwarzen Umrandungen.](images/face1.png)

 --- feedback ---

 Nicht ganz, schau dir die Reihenfolge der `ellipse()` und `stroke()` Funktionen an.

 --- /feedback ---

- ( )

![Ein weißes Gesicht mit schwarzer Umrandung. Da sind zwei grüne Augen mit schwarzen Pupillen. Beide haben eine schwarze Umrandung.](images/face2.png)

 --- feedback ---

 Nicht ganz, schau dir die Reihenfolge der `stroke()` Funktionen an.

 --- /feedback ---

- (x)

![Ein weißes Gesicht mit schwarzer Umrandung. Da sind zwei grüne Augen mit schwarzen Pupillen. Die Augen haben außerdem keine Umrandung.](images/face3.png)

 --- feedback ---

 Richtig! Der Code zeichnet ein Gesicht mit einer schwarzen Linie und schaltet dann die Linie aus, bevor er die Kreise zeichnet. Die grünen Kreise werden zuerst gezeichnet mit den schwarzen Kreisen obendrauf.

 --- /feedback ---

- ( )

![Ein weißes Gesicht mit schwarzer Umrandung. Da sind zwei grüne Augen, die keine Umrandung haben.](images/face4.png)

 --- feedback ---

 Nicht ganz, schau dir die Reihenfolge der `ellipse()` Funktionen an.

 --- /feedback ---

--- /choices ---

--- /question ---
