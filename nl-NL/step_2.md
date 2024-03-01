## Kies een thema

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Heb je een idee over het soort gezicht of masker dat je wilt maken? Gebruik deze stap om een plannetje te maken voor je kunstwerk en je canvas in te stellen.
</div>
<div>
![Het outputgebied met een gezicht met een vampierthema.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Open het [start project](https://editor.raspberrypi.org/en/projects/make-face-starter){:target="_blank"}. De code-editor wordt geopend in een ander browsertabblad.

--- /task ---

--- task ---

**Kies:** denk na over het soort gezicht dat je wilt maken:
+ Wil je iets kiezen uit je erfgoed of populaire cultuur?
+ Ga je een kunstwerk maken van een mens, dier, iets mythisch, of misschien een machine laten zien?
+ Misschien wil je wel een zelfportret maken!
+ Je kunt een emoji tekenen om met je vrienden te delen

--- /task ---

--- task ---

Het eerste wat je moet doen bij het maken van kunst met de Python `Processing library` is het toevoegen van `def setup():` om een `setup`-functie te definiëren die eenmaal aan het begin van je programma wordt uitgevoerd.

Het startproject heeft een `setup`-functie die de `grootte` van je canvas instelt op `400` breedte en `400` hoogte.

**Kies:** experimenteer met de getallen en voer je code uit om een grootte te vinden die je leuk vindt.

--- collapse ---

---
title: De schermgrootte instellen wanneer het programma wordt gestart
---

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 7
---
def setup():   
size(400, 400) #400 bij 400 werkt goed voor een rond gezicht

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Kies:** denk aan de kleuren die je voor je gezicht gaat gebruiken en wijzig de `achtergrond` kleurwaarden om het scherm in te stellen op een complementaire kleur.

[[[generic-theory-simple-colours]]]

--- collapse ---

---
title: De achtergrondkleur instellen wanneer het programma start
---

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 9
line_highlights: 9
---

    background(255, 255, 255) #Probeer andere getallen om de kleur te veranderen

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Tip:** de `draw` functie heeft `grid()` (raster) code. Hiermee wordt een coördinatenraster over je achtergrond toegevoegd dat je helpt uit te zoeken waar je elementen op je gezicht kunt plaatsen.

Om het raster uit te schakelen, voeg je een `#` toe voor de code, om deze weer in te schakelen, verwijder je de `#`.

--- code ---
---
language: python
filename: main.py - draw()
---

    grid() #Toont raster

--- /code ---

--- code ---
---
language: python
filename: main.py - draw()
---

    #grid() #Verberg raster door het te veranderen in een opmerking

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je project uit om de gekozen schermgrootte en achtergrondkleur te zien.

--- /task ---

--- task ---

**Debug:** je kunt enkele bugs in je project vinden die je moet oplossen. Hier zijn enkele veel voorkomende bugs.

--- collapse ---

---
title: Ik heb mijn grootte en kleur bijgewerkt, maar het uitvoergebied blijft hetzelfde
---

Nadat je de code hebt gewijzigd, moet je je project `uitvoeren` om de wijzigingen in het uitvoergebied te zien.

--- /collapse ---

--- collapse ---

---
title: Ik heb verschillende getallen geprobeerd, maar de achtergrondkleur verandert niet
---

De maximale hoeveelheid rood, groen of blauw is `255`. Zorg ervoor dat alle `achtergrond` kleurwaarden tussen `0` en `255` liggen.

--- /collapse ---

--- /task ---

--- save ---
