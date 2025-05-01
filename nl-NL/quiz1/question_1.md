## Snelle quiz

Beantwoord de drie vragen. Je wordt naar het juiste antwoord geleid.

Klik na het beantwoorden van elke vraag op **Controleer mijn antwoord**.

Veel plezier!

--- question ---

---
legend: Vraag 1 van 3
---

In je project heb je monden getekend met behulp van vormen.

Wat voor mond zou deze code tekenen?

--- code ---
---
language: python

---
def draw():
  fill(0, 0, 0) # Zwart
  ellipse(160, 200, 150, 150)
  fill(255, 255, 255) # Wit
  ellipse(160, 150, 150, 150)

--- /code ---

--- choices ---

- ( ) ![](images/sad-mouth.png)

  --- feedback ---

  Niet helemaal, om een droevige mond te maken zou de tweede `ellipse` een **y-coordinaat** nodig hebben die lager is dan de eerste `ellipse`.

  --- /feedback ---

- (x) ![](images/happy-mouth.png)

  --- feedback ---

  Dat klopt! De tweede `ellipse` wordt getekend met een **y-coordinaat** die hoger is dan de eerste `ellipse`.

  --- /feedback ---

- () ![](images/circle-mouth.png)

  --- feedback ---

   Niet helemaal, de tweede cirkel heeft een witte `fill(255, 255, 255)` en is gedeeltelijk over de eerste zwarte cirkel geplaatst.

  --- /feedback ---

- ( ) ![](images/square-mouth.png)

  --- feedback ---

De code tekent geen rechthoeken. De functie `ellipse` tekent cirkels.

  --- /feedback ---

--- /choices ---

--- /question ---
