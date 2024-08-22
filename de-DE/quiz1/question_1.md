## Kurzes Quiz

Beantworte die drei Fragen. Hinweise helfen dir beim Finden der richtigen Antwort.

Nach dem Beantworten der Fragen wähle **Meine Antwort prüfen**.

Viel Spaß!

Viel Spaß!

--- question ---

---
legend: Frage 1 von 3
---

In deinem Projekt hast du mithilfe von Formen Münder gezeichnet.

Welchen Mund würde dieser Code zeichnen?

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

  Richtig! The second `ellipse` is drawn with a **y_coordinate** that is higher than the first `ellipse`.

  --- /feedback ---

- () ![](images/circle-mouth.png)

  --- feedback ---

   Not quite, the second circle has a white `fill(255, 255, 255)` and is positioned partially over the first black circle.

  --- /feedback ---

- ( ) ![](images/square-mouth.png)

  --- feedback ---

Der Code zeichnet keine Rechtecke. Die Funktion `ellipse` zeichnet Kreise.

  --- /feedback ---

--- /choices ---

--- /question ---
