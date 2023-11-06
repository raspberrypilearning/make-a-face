## Siâp y wyneb

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Lluniwch a lliwio siâp ar gyfer eich wyneb neu fasg. Peidiwch ag ychwanegu'r nodweddion eraill eto, byddwch chi'n gwneud hynny nes 'mlaen.
</div>
<div>
![Delwedd o robot wyneb sgwâr.](images/robot-teeth.png){:width="200px"}
</div>
</div>

--- task ---

Penderfynwch ar brif siâp y wyneb ar gyfer eich masg. Fe allai fod yn gylch, yn elips, yn betryal, neu'n driongl hyd yn oed.

Ychwanegwch god at y swyddogaeth `draw()` i lunio wyneb neu fasg. Cofiwch dynnu `pass` o du mewn y swyddogaeth hefyd.

Mae'r enghraifft hon yn llunio cylch yn y canol, ond chi sydd i benderfynu pa siâp i'w ddefnyddio.

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

![Yr ardal allbwn yn dangos cylch du yng nghanol y grid.](images/black-circle.png)

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---

**Profi:** Rhedwch eich cod a'i newid i gael y maint a siâp wyneb o'ch dewis.

--- /task ---

--- task ---

Dewiswch liw strôc ar gyfer yr amlinell a lliw llenwi ar gyfer y brif ran o'r siâp.

[[[processing-stroke]]]

Os nad ydych chi eisiau amlinell, defnyddiwch `no_stroke()`.

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

**Test:** Run your code and change the colour until you are happy with it.

--- /task ---

--- save ---
