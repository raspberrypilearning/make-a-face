## Rechthoeken

Rechthoeken worden op bijna dezelfde manier getekend als ellipsen.

--- task ---

Wijzig de functie `ellipse` zodat deze de functie `rect` aanroept.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 17
---

def draw():
    # Zet hier code om bij elk frame uit te voeren
    background(255, 255, 255)  
    # Voeg hier code toe om je gezicht te tekenen
    fill(255, 255, 0) 
    rect(
        scherm_grootte/2, 
        scherm_grootte/2, 
        100, 
        50
    )  
  
--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit om een rechthoek te zien in plaats van een ellips.

--- /task ---

De eerste twee waarden voor `rect` en `ellipse` zijn de x-, y-coördinaten van het middelpunt van de vorm. Op dit moment zijn ze ingesteld op `scherm_grootte/2` om de vorm in het midden van het scherm te positioneren.

De linkerbovenhoek van het scherm is de coördinaat `0`,`0`. Als je de waarde van `x` verhoogt, wordt de vorm naar rechts verplaatst. Als je de waarde van `y` verhoogt, wordt de vorm naar beneden verplaatst.


--- task ---

Wijzig de positiewaarden om te bepalen waar de vorm op het scherm verschijnt.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 18-19
---

def draw():
    # Zet hier code om bij elk frame uit te voeren
    background(255, 255, 255)  
    # Voeg hier code toe om je gezicht te tekenen
    fill(255, 255, 0) 
    rect(
        80, # x-coördinaat
        60, # y-coördinaat
        100, 
        50
    )  
  
--- /code ---

--- /task ---

--- task ---

**Test:** Experimenteer met het wijzigen van de coördinaten en voer vervolgens jouw code uit om te zien waar de ellips of rechthoek wordt weergegeven.

--- /task ---