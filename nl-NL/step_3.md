## Cirkels en ovalen

Teken en kleur een vorm voor je gezicht of masker.

Een **ellips** is een ovale vorm. Als je dezelfde breedte en hoogte opgeeft, dan teken je een cirkel.

--- task ---

Voeg code toe aan de `draw()` functie om de opvulkleur in te stellen met rode, groene en blauwe waarden, net zoals je voor de achtergrond hebt gedaan.

Teken vervolgens een cirkel in deze kleur.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 16-22
---

def draw(): # Put code to run every frame here background(255, 255, 255)  
# Add code to draw your face here fill(255, 255, 0) ellipse( screen_size/2, screen_size/2, 200, 200 )

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit, je zou een gekleurde cirkel moeten zien.

--- /task ---

--- task ---

Wijzig de waarden voor breedte en hoogte om te zien hoe de ellips van vorm verandert.

--- code ---
---
language: python line_numbers: true line_number_start: 10
line_highlights: 18-19
---

def draw(): # Put code to run every frame here background(255, 255, 255)  
# Add code to draw your face here fill(255, 255, 0) ellipse( screen_size/2, screen_size/2, 100, # width 50   # height )

--- /code ---

![Een gele ellips die breder is dan hij hoog is.](images/change_shape.png)

--- /task ---

--- task ---

Vóór de code waarin je de ellips tekent, kun je een kleur en dikte instellen.


--- code ---
---
language: python line_numbers: true line_number_start: 14
line_highlights: 15-16
---

    fill(255, 255, 0) 
    stroke(255, 255, 255)  
    stroke_weight(3)
    ellipse(
        screen_size/2, 
        screen_size/2, 
        100, 
        50
    )

--- /code ---

Of, als je dat liever wilt, kun je de lijn verwijderen, zodat er geen omtrek meer overblijft.

--- code ---
---
language: python line_numbers: true line_number_start: 14
line_highlights: 15
---

    fill(255, 255, 0) 
    no_stroke()
    ellipse(
        screen_size/2, 
        screen_size/2, 
        100, 
        50
    )

--- /code ---

--- /task ---

--- task ---

**Test:** Experimenteer met het wijzigen van de kleur en dikte van de lijn of deze te verwijderen, voer vervolgens je code uit om de resultaten te bekijken.

--- /task ---