## Kurzes Quiz

Beantworte die drei Fragen. Hinweise helfen dir beim Finden der richtigen Antwort.

Nach dem Beantworten jeder Frage wähle **Meine Antwort prüfen**.

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
def draw():
  fill(0, 0, 0) # Schwarz
  ellipse(160, 200, 150, 150)
  fill(255, 255, 255) # Weiß
  ellipse(160, 150, 150, 150)

--- /code ---

--- choices ---

- ( ) ![](images/sad-mouth.png)

  --- feedback ---

  Nicht ganz. Um einen traurigen Mund zu erzeugen, würde die zweite `ellipse` eine **y-Koordinate** benötigen, die niedriger ist als die erste `ellipse`.

  --- /feedback ---

- (x) ![](images/happy-mouth.png)

  --- feedback ---

  Richtig! Die zweite `ellipse` wird mit einer **y-Koordinate** gezeichnet, die höher ist als die erste `ellipse`.

  --- /feedback ---

- () ![](images/circle-mouth.png)

  --- feedback ---

   Nicht ganz, der zweite Kreis hat eine weiße `fill(255, 255, 255)` und ist teilweise über dem ersten schwarzen Kreis positioniert.

  --- /feedback ---

- ( ) ![](images/square-mouth.png)

  --- feedback ---

Der Code zeichnet keine Rechtecke. Die Funktion `ellipse` zeichnet Kreise.

  --- /feedback ---

--- /choices ---

--- /question ---
