## Überlappende Formen

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Der Mund ist eine gute Möglichkeit, Emotionen darzustellen. Wird deine Figur lächeln, die Stirn runzeln, oder etwas anderes machen? 
</div>
<div>
![Bild, das ein Robotergesicht als Beispiel für ein Gesicht mit Mund zeigt.](images/mask.png){:width="200px"}
</div>
</div>

Durch Überlappen von Formen kannst du Formen erstellen, die sonst nicht möglich wären. Du kannst zum Beispiel zwei überlappende Kreise hinzufügen, um ein Lächeln zu erzeugen.

--- task ---

Beginne mit einer Ellipse, die das Gesicht darstellt.


--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 17-18
---
def draw():
    # Füge hier den Code ein, der bei jedem Frame ausgeführt werden soll
    background(255, 255, 255)
    # Füge hier den Code hinzu, um dein Gesicht zu zeichnen
    no_stroke()
    fill(125, 75, 0) # Braun
    ellipse(200, 220, 150, 150) # Gesicht

--- /code ---

--- /task ---

--- task ---

Lege die Füllfarbe für deinen Mund mit `fill` (englisch: füllen) fest und zeichne dann eine Ellipse mit `ellipse`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 19-22
---
def draw():
    # Füge hier den Code ein, der bei jedem Frame ausgeführt werden soll
    background(255, 255, 255)
    # Füge hier den Code hinzu, um dein Gesicht zu zeichnen
    no_stroke()
    fill(125, 75, 0) # Braun
    ellipse(200, 220, 150, 150) # Gesicht
    fill(255, 0, 0)  # Rot
    ellipse(200, 240, 40, 40) # Mund

--- /code ---

--- /task ---

--- task ---

Stelle `fill` so ein, dass sie zur Gesichtsfarbe passt, und zeichne dann eine zweite `ellipse`.

Ändere die `y`-Koordinate der zweiten `ellipse` zu einer etwas höheren Position, um ein Lächeln zu zeichnen.


--- code ---
---
language: python
line_numbers: true
line_number_start: 18
line_highlights: 20-21
---
    fill(255, 0, 0)  # Rot
    ellipse(200, 240, 40, 40) # Mund
    fill(125, 75, 0) # Braun
    ellipse(200, 235, 40, 40) # Überlappung   

--- /code ---

![Ein brauner Kreis mit einer roten Mondsichel am unteren Rand, wie ein Lächeln](images/brown-circle-smile.png)

--- /task ---

--- task ---

**Test:** Experimentiere mit den Füllfarben und Größen der Ellipsen. Führe dein Programm aus, um die Ergebnisse anzuzeigen.

--- /task ---