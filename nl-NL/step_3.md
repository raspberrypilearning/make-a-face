## Vorm van het gezicht

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Teken en kleur een vorm voor je gezicht of masker. Voeg de andere elementen nog niet toe, die komen later.
</div>
<div>
![Afbeelding van een robot met een vierkant gezicht.](afbeeldingen/robot-tanden.png){:width="200px"}
</div>
</div>

--- task ---

Kies de hoofdvorm van het gezicht voor je masker. Het kan een cirkel, een ellips, een rechthoek of zelfs een driehoek zijn.

Voeg code toe aan de `draw()` functie om een gezicht of masker te tekenen.

In dit voorbeeld wordt een zwarte cirkel in het midden getekend, maar je kunt helemaal zelf bepalen welke vorm en kleur je wil gebruiken.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 10
line_highlights: 14, 15
---

def draw():
    # Zet hier code om bij elk frame uit te voeren
    background(255, 255, 255)  # Verander naar de achtergrondkleur
    
    # Voeg hier code toe om je gezicht te tekenen
    ellipse(width/2, height/2, 200, 200)  # Cirkel in het midden
    
    grid()  # voeg een # toe aan het begin van deze regel om het raster te verbergen
  
--- /code ---

![Het uitvoergebied met een zwarte cirkel in het midden van het raster.](images/black-circle.png)

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---

**Test:** Voer je code uit en wijzig deze om de grootte en vorm van het gezicht te krijgen die je wilt.

--- /task ---

--- task ---

Kies een lijnkleur voor de omtrek en een vulkleur voor het hoofdgedeelte van de vorm.

[[[processing-stroke]]]

Als je geen omtrek wilt, gebruik dan `no_stroke()`.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 13
line_highlights: 14
---

    # Voeg hier code toe om je gezicht te tekenen
    fill(255, 255, 0)  # Fel geel
    ellipse(width/2, height/2, 200, 200)
  
--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Voer je code uit en wijzig de kleur totdat je er tevreden mee bent.

--- /task ---

--- save ---
