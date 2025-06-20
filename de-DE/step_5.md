## Dreiecke

Um ein Dreieck zu zeichnen, musst du drei Wertepaare angeben. Jedes Paar ist eine x,y-Koordinate für einen der Punkte des Dreiecks.

--- task ---

Füge Code hinzu, um ein `triangle` (englisch für Dreieck) zu zeichnen.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 17-21
---

def draw():
    # Füge hier den Code ein, der bei jedem Frame ausgeführt werden soll
    background(255, 255, 255)  
    # Füge hier den Code hinzu, um dein Gesicht zu zeichnen
    fill(255, 255, 0) 
    triangle(
        210, 250, 
        330, 150, 
        220, 160
    )  
  
--- /code ---

--- /task ---

--- task ---

**Test:** Experimentiere mit den Koordinaten und führe dann deinen Code aus, um zu sehen, wie durch Verbinden der Punkte an diesen Koordinaten ein Dreieck entsteht.

--- /task ---
