--- question ---

---
legend: Vraag 2 van 3
---

In je project heb je code toegevoegd om een gezicht te tekenen met veel kenmerken. De volgorde van je code was erg belangrijk om het gezicht er precies zo uit te laten zien als je ontwerp.

Hoe zou het gezicht eruit zien als je deze code uitvoert?

--- code ---
---
language: python

---

def draw():

  # Gezicht
  stroke(0) # Zwart
  fill(255) # Wit
  ellipse(200, 200, 200, 190)
  no_stroke()
  
  # Ogen
  fill(0, 255, 0) # Groen
  ellipse(160, 180, 60, 60)
  ellipse(240, 180, 60, 60)
  fill(0) # Zwart
  ellipse(160, 180, 30, 30)
  ellipse(240, 180, 30, 30)
  
run()

--- /code ---

--- choices ---

- ( )

![Een wit gezicht met een zwarte omtrek. Er zijn twee groene ogen met zwarte contouren.](images/face1.png)

 --- feedback ---

 Niet helemaal, kijk naar de volgorde van de `ellipse()` en de `stroke()` functies.

 --- /feedback ---

- ( )

![Een wit gezicht met een zwarte omtrek. Er zijn twee groene ogen met zwarte pupillen en beide hebben een zwarte omtrek.](images/face2.png)

 --- feedback ---

 Niet helemaal, kijk naar de volgorde van de `stroke()` functies.

 --- /feedback ---

- (x)

![Een wit gezicht met een zwarte omtrek. Er zijn twee groene ogen met zwarte pupillen en de ogen hebben geen omtreklijn.](images/face3.png)

 --- feedback ---

 Juist, de code tekent een gezicht met een zwarte streep en schakelt de rand uit voordat de cirkels worden getekend. De groene cirkels worden eerst getekend met de zwarte cirkels er bovenop.

 --- /feedback ---

- ( )

![Een wit gezicht met een zwarte omtrek. Er zijn twee groene ogen die geen omtrek hebben.](images/face4.png)

 --- feedback ---

 Niet helemaal, kijk naar de volgorde van de `ellipse()` functies.

 --- /feedback ---

--- /choices ---

--- /question ---
