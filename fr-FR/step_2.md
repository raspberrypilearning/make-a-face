## Choisir une couleur d'arrière-plan

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
As-tu une idée du type de visage ou de masque que tu souhaites réaliser ? Utilise cette étape pour planifier ton œuvre et configurer ta zone de travail.
</div>
<div>
![La zone de sortie avec un visage sur le thème des vampires.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Ouvre le [projet de démarrage](https://editor.raspberrypi.org/en/projects/make-face-starter){:target="_blank"}.

--- /task ---

--- task ---

Les trois nombres dans `background(0, 0, 0)` sont les valeurs rouge, verte et bleue. Expérimente en remplaçant les nombres par n'importe quel nombre entier compris entre 0 et 255 pour modifier la couleur d'arrière-plan.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 14
---

def draw():   
# Put code to run every frame here background(0, 0, 0)

--- /code ---

--- /task ---

--- task ---

**Test :** exécute ton code et tu devrais voir un carré coloré comme arrière-plan.

--- /task ---
