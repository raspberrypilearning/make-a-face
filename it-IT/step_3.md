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
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 10
line_highlights: 14, 15
---

def draw():
    # Metti qui sotto il codice che verrà eseguito per ogni frame
    background(255, 255, 255)  # Cambia il colore dello sfondo
    
    # Aggiungi qui il codice per disegnare la tua faccia
    ellipse(width/2, height/2, 200, 200)  # Cerchio nel mezzo
    
    grid()  # aggiungi un # all'inizio di questa riga per nascondere la griglia
  
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

Se non vuoi un contorno, inserisci il comando `no_stroke()`.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 13
line_highlights: 14
---

    # Aggiungi qui il codice per disegnare la tua faccia
    fill(255, 255, 0)  # Giallo acceso
    ellipse(width/2, height/2, 200, 200)
  
--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Esegui il tuo codice e cambia il colore fino a quando non ne sei soddisfatto.

--- /task ---

--- save ---
