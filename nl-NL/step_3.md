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

Voeg code toe aan de `draw()` functie om een gezicht of masker te tekenen. Zorg ervoor dat je ook `pass` verwijdert in de functie.

In dit voorbeeld wordt een cirkel in het midden getekend, maar je kunt helemaal zelf bepalen welke vorm je wil gebruiken.

--- code ---
---
language: python 
filename: main.py - draw() 
line_numbers: true 
line_number_start: 11
line_highlights: 12
---

def draw():   
  ellipse(width/2, height/2, 200, 200) #Cirkel in het midden

--- /code ---

![Het output gebied met een zwarte cirkel in het midden van het raster.](images/black-circle.png)

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
line_number_start: 11
line_highlights: 13
---

def draw(): 
  stroke(0) #Je kunt ook no_stroke() gebruiken
  fill(255, 255, 0) #Fel geel 
  ellipse(width/2, height/2, 200, 200) #Cirkel in het midden

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Voer je code uit en wijzig de kleur totdat je er tevreden mee bent.

--- /task ---

--- save ---
