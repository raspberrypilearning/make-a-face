## Forma del viso

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Disegna e colora una forma per il viso o la maschera. Non aggiungere ancora le altre funzionalità, verranno più tardi.
</div>
<div>
![Immagine della faccia quadrata di un robot.](images/robot-teeth.png){:width="200px"}
</div>
</div>

--- task ---

Decidi la forma principale del viso per la tua maschera. Potrebbe essere un cerchio, un'ellisse, un rettangolo o persino un triangolo.

Aggiungi il codice alla funzione `draw()` per disegnare una faccia o una maschera.

Questo esempio disegna un cerchio nero nel mezzo, ma sta a te scegliere quale forma e colore usare.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 10
line_highlights: 14, 15
---

def draw(): # Put code to run every frame here background(255, 255, 255)  # Change to your background colour

    # Add code to draw your face here
    ellipse(width/2, height/2, 200, 200)  # Circle in the middle
    
    grid()  # add a # to the beginning of this line to hide the grid

--- /code ---

![L'output che mostra una circonferenza con bordo nero al centro della griglia.](images/black-circle.png)

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---

**Test:** Esegui il codice e cambialo per ottenere la dimensione e la forma del viso che desideri.

--- /task ---

--- task ---

Scegli un colore per il contorno e un colore di riempimento per la parte principale della forma.

[[[processing-stroke]]]

Se non vuoi un contorno, inserisci il comando `no_stroke ()`.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 13
line_highlights: 14
---

    # Add code to draw your face here
    fill(255, 255, 0)  # Bright yellow
    ellipse(width/2, height/2, 200, 200)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Esegui il tuo codice e cambia il colore fino a quando non ne sei soddisfatto.

--- /task ---

--- save ---
