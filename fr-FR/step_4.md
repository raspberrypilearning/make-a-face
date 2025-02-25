## Rectangles

Les rectangles sont dessinés presque de la même manière qu'une ellipse.

--- task ---

Modifie la fonction `ellipse` pour appeler à la place la fonction `rect`.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 17
---

def draw(): # Put code to run every frame here background(255, 255, 255)  
# Add code to draw your face here fill(255, 255, 0) rect( screen_size/2, screen_size/2, 100, 50 )

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton code pour voir un rectangle au lieu d’une ellipse.

--- /task ---

Les deux premières valeurs pour `rectangle` et `ellipse` représentent les coordonnées x, y du centre de la forme. Pour le moment, ils sont définis sur `taille_ecran/2` pour positionner la forme au centre de l'écran.

Le coin supérieur gauche de l'écran a pour coordonnées `0`,`0`. L'augmentation de la valeur `x` déplacera la forme vers la droite. L'augmentation de la valeur `y` déplacera la forme vers le bas.


--- task ---

Modifie les valeurs de position pour modifier l’endroit où la forme apparaît sur l’écran.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 18-19
---

def draw(): # Put code to run every frame here background(255, 255, 255)  
# Add code to draw your face here fill(255, 255, 0) rect( 80, # x coordinate 60, # y coordinate 100, 50 )

--- /code ---

--- /task ---

--- task ---

**Test :** expérimente en modifiant les coordonnées, puis exécute ton code pour voir où l'ellipse ou le rectangle est affiché.

--- /task ---