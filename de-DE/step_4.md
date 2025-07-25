## Rechtecke

Rechtecke werden fast auf die gleiche Weise wie Ellipsen gezeichnet.

--- task ---

Ändere die Funktion `ellipse`, um stattdessen die Funktion `rect`aufzurufen.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 17
---

def draw():
    # Füge hier den Code ein, der bei jedem Frame ausgeführt werden soll
    background(255, 255, 255)  
    # Füge hier den Code hinzu, um dein Gesicht zu zeichnen
    fill(255, 255, 0) 
    rect(
        bildschirm_groesse/2, 
        bildschirm_groesse/2, 
        100, 
        50
    )  
  
--- /code ---

--- /task ---

--- task ---

**Test:** Führe deinen Code aus, um ein Rechteck statt einer Ellipse anzuzeigen.

--- /task ---

Die ersten beiden Werte für `rect` und `ellipse` stellen die x- und y-Koordinaten des Mittelpunkts der Form dar. Momentan sind sie auf `bildschirm_groesse/2` eingestellt, um die Form in der Bildschirmmitte zu positionieren.

Die obere linke Ecke des Bildschirms hat die Koordinate `0`,`0`. Wenn du den Wert für `x` erhöhst, wird die Form nach rechts verschoben. Wenn Sie den Wert für `y` erhöhst, wird die Form nach unten verschoben.


--- task ---

Ändere die Positionswerte, um zu verändern, wo die Form auf dem Bildschirm erscheint.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 18-19
---

def draw():
    # Füge hier den Code ein, der bei jedem Frame ausgeführt werden soll
    background(255, 255, 255)  
    # Füge hier den Code hinzu, um dein Gesicht zu zeichnen
    fill(255, 255, 0) 
    rect(
        80, # x-Koordinate
        60, # y-Koordinate
        100, 
        50
    )  
  
--- /code ---
--- /task ---

--- task ---

**Test:** Experimentiere mit der Änderung der Koordinaten und führe dann deinen Code aus, um zu sehen, wo die Ellipse oder das Rechteck angezeigt wird.

--- /task ---