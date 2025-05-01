## Triangles

Pour dessiner un triangle, tu dois donner trois paires de valeurs. Chaque paire est une coordonnée x, y pour l'un des points du triangle.

--- task ---

Ajoute du code pour dessiner un `triangle`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 17-21
---

def draw():
    # Mettre le code pour exécuter chaque image ici
    background(255, 255, 255)  
    # Ajoute du code pour dessiner ton visage ici
    fill(255, 255, 0) 
    triangle(
        210, 250, 
        330, 150, 
        220, 160
    )  
  
--- /code ---

--- /task ---

--- task ---

**Test :** expérimente en modifiant les coordonnées, puis exécute ton code pour voir un triangle affiché en joignant les points à ces coordonnées.

--- /task ---
