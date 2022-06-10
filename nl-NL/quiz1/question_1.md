## Reflectie

Goed gedaan, je hebt veel geleerd! Nu is het tijd om te reflecteren - reflecteren is een belangrijk onderdeel van leren, omdat het helpt om nieuwe verbindingen in je hersenen te maken.

Beantwoord de drie onderstaande vragen om terug te kijken op wat je hebt geleerd.

Druk na elke vraag op **indienen**. Je wordt naar het juiste antwoord geleid. Je kunt deze activiteit zo vaak doen als je wilt.

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
  fill(0, 0, 0) #Zwart
  ellipse(160, 200, 150, 150)
  fill(255, 255, 255) #Wit
  ellipse(160, 150, 150, 150)

--- /code ---

--- choices ---

- ( ) ![](images/sad-mouth.png)

  --- feedback ---

  Niet helemaal, om een droevige mond te maken zou de tweede `ellips` een **y-coordinaat** nodig hebben die lager is dan de eerste `ellips`.

  --- /feedback ---

- (x) ![](images/happy-mouth.png)

  --- feedback ---

  Dat klopt! De tweede `ellips` wordt getekend met een **y-coordinaat** die hoger is dan de eerste `ellips`.

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
