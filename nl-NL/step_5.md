## Driehoeken

Om een driehoek te tekenen, moet je drie waardeparen opgeven. Elk paar is een x,y-coördinaat voor een van de punten van de driehoek.

--- task ---

Voeg code toe om een `triangle` te tekenen.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 17-21
---

def draw():
    # Zet hier code om bij elk frame uit te voeren
    background(255, 255, 255)  
    # Voeg hier code toe om je gezicht te tekenen
    fill(255, 255, 0) 
    triangle(
        210, 250, 
        330, 150, 
        220, 160
    )  
  
--- /code ---

--- /task ---

--- task ---

**Test:** Experimenteer met het veranderen van de coördinaten en voer vervolgens jouw code uit om te zien hoe een driehoek wordt weergegeven door de punten op die coördinaten met elkaar te verbinden.

--- /task ---
