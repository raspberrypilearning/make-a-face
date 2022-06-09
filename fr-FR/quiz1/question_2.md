--- question ---

---
legend: Question 2 sur 3
---

Dans ton projet, tu as ajouté du code pour dessiner un visage avec de nombreuses caractéristiques. L'ordre de ton code était extrêmement important pour que le visage ressemble à ton design.

Si tu exécutais ce code, à quoi ressemblerait le visage ?

--- code ---
---
language: python

---

def draw():

  #Visage
  stroke(0) #Noir
  fill(255) #Blanc
  ellipse(200, 200, 200, 190)
  no_stroke()
  
  #Yeux
  fill(0, 255, 0) #Vert
  ellipse(160, 180, 60, 60)
  ellipse(240, 180, 60, 60)
  fill(0) #Noir
  ellipse(160, 180, 30, 30)
  ellipse(240, 180, 30, 30)
  
run()

--- /code ---

--- choices ---

- ( )

![Un visage blanc aux contours noirs. Il y a deux yeux verts avec des contours noirs.](images/face1.png)

 --- feedback ---

 Pas tout à fait, regarde l'ordre des fonctions `ellipse()` et `stroke()`.

 --- /feedback ---

- ( )

![Un visage blanc aux contours noirs. Il y a deux yeux verts avec des pupilles noires et les deux ont un contour noir.](images/face2.png)

 --- feedback ---

 Pas tout à fait, regarde l'ordre des fonctions `stroke()`.

 --- /feedback ---

- (x)

![Un visage blanc aux contours noirs. Il y a deux yeux verts avec des pupilles noires et les yeux n'ont pas de contour.](images/face3.png)

 --- feedback ---

 Correct, le code dessine un visage avec un trait noir puis désactive le trait avant de dessiner les cercles. Les cercles verts sont dessinés en premier avec les cercles noirs au-dessus d'eux.

 --- /feedback ---

- ( )

![Un visage blanc aux contours noirs. Il y a deux yeux verts qui n'ont pas de contour.](images/face4.png)

 --- feedback ---

 Pas tout à fait, regarde l'ordre des fonctions `ellipse()`.

 --- /feedback ---

--- /choices ---

--- /question ---
