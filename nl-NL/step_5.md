## Voeg een mond toe

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Een mond is een geweldige manier om emotie te tonen. Zal je gezicht een glimlach, frons of iets anders hebben? 
</div>
<div>
![Afbeelding met een robotgezicht als voorbeeld van een gezicht met een mond.](images/mask.png){:width="200px"}
</div>
</div>

--- task ---

Bedenk wat voor soort mond je gezicht nodig heeft. De eenvoudigste mond zou een cirkel zijn om verrast te kijken.

Je kunt twee overlappende cirkels toevoegen om een glimlach of frons te maken. Er kunnen driehoeken of rechthoeken worden toegevoegd voor tanden.

--- /task ---

--- task ---

Voeg code toe aan je `draw()` functie om een mond toe te voegen.

--- collapse ---

---
title: Maak een mond van overlappende cirkels
---

Stel de `vul`-kleur in voor je mond en teken vervolgens een `ellips`. Stel de `vul`-kleur opnieuw in, deze keer om overeen te komen met de gezichtskleur, en teken vervolgens een tweede `ellips`.

Verander de `y` coördinaat van de tweede `ellips` naar een iets hogere positie voor een glimlach of een iets lagere positie voor een frons.

![Het outputgebied toont een lachende mond.](images/smile.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0) #Een zwarte mond
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0) #Een oranje gezicht
    ellipse(200, 235, 15, 15) #Hogere cirkel

--- /code ---

![Het outputgebied met een fronsende mond.](images/frown.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0) #Een zwarte mond
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0) #Een oranje gezicht
    ellipse(200, 245, 15, 15) #Onderste cirkel

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Maak een mond met behulp van rechthoeken
---

Robots worden vaak afgebeeld met `rechthoekige` monden. Soms worden `rechthoek`- en `ellips`-vormen samen gebruikt om een grijns-emoji te maken of om een gezichtsmasker toe te voegen.

![Het outputgebied toont een gezicht met een rechthoekig gezichtsmasker.](images/rectangle-mask.png)

Voeg de code toe voor een `rechthoek` en maak er vervolgens een kleinere `rechthoek` in. Wijzig de kleuren van de `lijn` en `vulling` om je thema aan te vullen. Voeg indien nodig `ellips`-vormen toe.

**Tip:** Vergeet niet om de `ellips`-vormen boven de `rechthoek`-code te plaatsen als je wil dat ze achter de `rechthoek`-vormen gaan.

--- code ---
---
language: python
filename: main.py - draw()
---
    # Gezichtsmasker
    no_fill()
    stroke(255, 255, 255)
    ellipse(150, 250, 30, 30)  # Linker oorlus
    ellipse(250, 250, 30, 30)  # Rechter oorlus
    fill(255, 255, 255)
    no_stroke()
    rect(150, 230, 100, 40)  # Grote witte rechthoek
    fill(108, 200, 206)
    rect(152, 235, 96, 30)  # Kleinere blauwe rechthoek

--- /code ---

--- /collapse ---

**Tip:** Voeg een `#Mond` opmerking toe voor code die je mond maakt om je te helpen deze code gemakkelijk terug te vinden.

--- /task ---

--- task ---

**Kies:** je kunt ook meerdere tanden aan je mond toevoegen met `translate` om de `x` coördinaat te veranderen na het tekenen van elke tand.

--- collapse ---

---
title: Gebruik een lus om een rij tanden toe te voegen
---

Voeg code toe om een `for` lus te maken die wordt herhaald om het aantal tanden te maken dat je nodig hebt.

![Het uitvoergebied toont een robotgezicht met een rij rechthoekige tanden in verschillende kleuren.](images/robot-teeth.png)

Voeg code toe om na elke getekende tand een `translate()` met de breedte van de tand uit te voeren.

Je kunt ook code toevoegen om de kleur van elke tand te veranderen.

--- code ---
---
language: python
filename: main.py - draw()
---

    # Mond
    fill(90, 110, 184)
    rood = 90  # Beginhoeveelheid rood
    groen = 110  # Beginhoeveelheid groen
    blauw = 180  # Beginhoeveelheid blauw
    for i in range (0,6):
        rect(100, 300, 33, 50)
        fill(rood, groen, blauw)  # Gebruikt variabelen om de kleurverandering van elke lus te regelen
        rood = rood+40
        blauw = blauw-30
        translate(33, 0)  # Beweeg langs de x-coördinaat met de breedte van een tand


--- /code ---

--- /collapse ---

[[[processing-translation]]]

--- collapse ---

---
title: Gebruik driehoeken om hoektanden toe te voegen
---

Maak een `rechthoek` om als mondlijn te gebruiken.

Voeg twee `driehoek`-vormen toe om de hoektanden te maken. Wijzig de `x`-coördinaten voor elke hoek om de tanden aan de tegenoverliggende uiteinden van de mondlijn te plaatsen.

![Het uitvoergebied toont een vampiergezicht met een rechthoekige mond en twee driehoekige tanden.](images/vampire.png)

--- code ---
---
language: python
filename: main.py - draw()
---
    # Mond
    fill(0)
    rect(170, 260, 60, 5)  # Mondlijn
    fill(0)
    triangle(170, 260, 180, 280, 190, 260)  # Linker tand
    triangle(210, 260, 220, 280, 230, 260)  # Rechter tand
--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Debug:** Mogelijk vind je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

--- collapse ---

---
title: Mijn overlappende vorm valt buiten het gezicht
---

Als je twee overlappende vormen gebruikt om een mond te maken, moet je ervoor zorgen dat de vorm die dezelfde kleur heeft als het gezicht niet buiten het gezicht valt. Als dit het geval is, wijzig dan de breedte of hoogte van de vorm zodat deze klein genoeg is om in het gezicht te passen.

--- /collapse ---


--- collapse ---

---
title: Ik heb te veel tanden
---

Vergeet niet dat `range()` een reeks getallen maakt die begint vanaf 0 en niet vanaf 1. Dit kan een verschil maken voor je code, afhankelijk van hoe je je tanden hebt gepositioneerd.

--- /collapse ---

--- /task ---

--- save ---
