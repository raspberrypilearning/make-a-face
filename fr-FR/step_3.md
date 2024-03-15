## Forme du visage

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Dessine et colorie une forme pour ton visage ou ton masque. N'ajoute pas encore les autres fonctionnalités, elles viendront plus tard.
</div>
<div>
![Image d'un robot à visage carré.](images/robot-teeth.png){:width="200px"}
</div>
</div>

--- task ---

Décide de la forme principale du visage pour ton masque. Il peut s'agir d'un cercle, d'une ellipse, d'un rectangle ou même d'un triangle.

Ajoute du code à la fonction `draw()` pour dessiner un visage ou un masque.

Cet exemple dessine un cercle noir au milieu, mais c'est à toi de choisir la forme et la couleur à utiliser.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 11
line_highlights: 12
---

def draw(): # Put code to run every frame here background(255, 255, 255)  # Change to your background colour

    # Add code to draw your face here
    ellipse(width/2, height/2, 200, 200)  # Circle in the middle
    
    grid()  # add a # to the beginning of this line to hide the grid

--- /code ---

![La zone de sortie montrant un cercle noir au milieu de la grille.](images/black-circle.png)

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---

**Test :** exécute ton code et modifie-le pour obtenir la taille et la forme de visage que tu souhaites.

--- /task ---

--- task ---

Choisis une couleur de trait pour le contour et une couleur de remplissage pour la partie principale de la forme.

[[[processing-stroke]]]

Si tu ne veux pas de contour, utilise `no_stroke()`.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 11
line_highlights: 13
---

    # Add code to draw your face here
    fill(255, 255, 0)  # Bright yellow
    ellipse(width/2, height/2, 200, 200)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test :** exécute ton code et modifie la couleur jusqu'à ce que tu en sois satisfait.

--- /task ---

--- save ---
