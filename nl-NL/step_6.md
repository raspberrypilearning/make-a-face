## Overlappende vormen

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Een mond is een geweldige manier om emotie te tonen. Zal je gezicht een glimlach, frons of iets anders hebben? 
</div>
<div>
![Afbeelding met een robotgezicht als voorbeeld van een gezicht met een mond.](images/mask.png){:width="200px"}
</div>
</div>

Door vormen te overlappen, kun je vormen maken die je anders niet zou kunnen maken, je kunt bijvoorbeeld twee overlappende cirkels toevoegen om een glimlach te creëren.

--- task ---

Begin met een ellips om het gezicht weer te geven.


--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 17-18
---
def draw():
    # Zet hier code om bij elk frame uit te voeren
    background(255, 255, 255)
    # Voeg hier code toe om je gezicht te tekenen
    no_stroke()
    fill(125, 75, 0) # Bruin
    ellipse(200, 220, 150, 150) # Gezicht

--- /code ---

--- /task ---

--- task ---

Stel de `fill`-kleur in voor je mond en teken vervolgens een `ellipse`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 19-22
---
def draw():
    # Zet hier code om bij elk frame uit te voeren
    background(255, 255, 255)
    # Voeg hier code toe om je gezicht te tekenen
    no_stroke()
    fill(125, 75, 0) # Bruin
    ellipse(200, 220, 150, 150) # Gezicht
    fill(255, 0, 0)  # Rood
    ellipse(200, 240, 40, 40) # Mond

--- /code ---

--- /task ---

--- task ---

Stel de `fill`-kleur in, zodat deze overenkomt met de gezichtskleur, en teken vervolgens een tweede `ellipse`.

Verander de `y` coördinaat van de tweede `ellipse` naar een iets hogere positie voor een glimlach.


--- code ---
---
language: python
line_numbers: true
line_number_start: 18
line_highlights: 20-21
---
    fill(255, 0, 0)  # Rood
    ellipse(200, 240, 40, 40) # Mond
    fill(125, 75, 0) # Bruin
    ellipse(200, 235, 40, 40) # Overlap   

--- /code ---

![Een bruine cirkel met een rode halve maan onderaan, als een glimlach](images/brown-circle-smile.png)

--- /task ---

--- task ---

**Test:** Experimenteer met het wijzigen van de vulkleuren en -groottes van de ellipsen. Voer jouw programma uit om de resultaten te bekijken.

--- /task ---