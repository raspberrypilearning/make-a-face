## Ajouter des yeux

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Les yeux font qu'une forme commence à ressembler à un visage.
</div>
<div>
![La zone de sortie montrant un visage avec des yeux.](images/eyes.png){:width="200px"}
</div>
</div>

--- task ---

Pense au type d'yeux dont ton visage a besoin. Les yeux les plus simples ne sont que deux cercles.

Tu peux ajouter des iris et des pupilles de différentes couleurs. Tu peux ajouter des zones claires / reflets dans une couleur différente.

--- /task ---

Expérimente avec `ellipse` dans la fonction `configuration` pour créer les yeux que tu veux.

--- task ---

### Positionner les yeux

Le premier nombre dans `ellipse` est le centre de l'œil. Les yeux doivent être positionnés à la même distance du centre du dessin.

Dans cet exemple, `160` et `240` sont tous les deux à `40` pixels de 200, ce qui fonctionne pour un dessin d'une largeur de 400.

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0) # Noir - passe au rouge, au vert ou au bleu jusqu'à 255
    taille-yeux = 50
    ellipse(160, 180, taille-yeux, taille-yeux) # x, y, largeur, hauteur
    ellipse(240, 180, taille-yeux, taille-yeux)

--- /code --- 

**Astuce :** si tu veux des yeux ronds, l'utilisation d'une variable `taille_yeux` facilite la modification de la largeur et de la hauteur des deux yeux au même endroit.

[[[processing-python-ellipse]]]

--- collapse ---

---
title: Calcul des positions en fonction de la largeur
---

Le centre d'un dessin est à la position `width / 2` ou la moitié de la largeur. Tu peux l'utiliser pour positionner les yeux en soustrayant la largeur des yeux pour l'œil gauche et en l'ajoutant pour l'œil droit :

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0) # Noir - passe au rouge, au vert ou au bleu jusqu'à 255
    taille-yeux = 50
    ellipse( (width / 2) - 40, 180, taille-yeux, taille-yeux) # x, y, largeur, hauteur
    ellipse( (width / 2) + 40 , 180, taille-yeux, taille-yeux)

--- /code ---

Tu peux également calculer la largeur des yeux en fonction de la largeur du dessin.

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0) # Noir - passe au rouge, au vert ou au bleu jusqu'à 255
    ellipse( (width / 2) - (width / 10) , 180, taille-yeux, taille-yeux) # x, y, largeur, hauteur
    ellipse( (width / 2) + (width / 10) , 180, taille-yeux, taille-yeux)

--- /code ---

--- /collapse ---

Modifie le deuxième nombre dans l'appel de fonction `ellipse` pour déplacer la position `y` (verticale) des yeux.

--- /task ---

--- task ---

**Test :** continue à changer la forme et la position des yeux jusqu'à ce que tu aimes leur apparence.

**Astuce :** si tu définis un trait pour dessiner le visage et que tu n'en veux pas pour les yeux, tu devras alors appeler `no_stroke()` avant de dessiner les yeux.

[[[processing-stroke]]]

--- /task ---

--- task ---

### Ajouter des détails

Tu peux utiliser d'autres cercles pour créer :
+ Des iris colorés
+ Des pupilles noires
+ Des reflets blancs
+ Ou autre chose

Cet œil a un iris coloré, une pupille noire et des reflets blancs avec une opacité modifiée :
![La zone de sortie montrant un œil avec des reflets au-dessus de la pupille et de l'iris.](images/catchlights.png)

[[[generic-theory-simple-colours]]]
[[[processing-opacity]]]

Tu peux également animer les yeux en les faisant pivoter.

[[[processing-rotation]]]

--- /task ---

--- task ---

**Test :** continue à changer les yeux jusqu'à ce que tu aimes leur apparence.

Ton dessin commence à ressembler à un visage ?

--- /task ---

--- task ---

**Débogage :** il est possible que tu trouves des bogues dans ton projet que tu dois corriger. Voici quelques bogues assez courants.

--- collapse ---
---
title: Les yeux ne sont pas centrés
---

Tu peux utiliser `height / 2` pour les placer au centre.

--- /collapse ---

--- collapse ---
---
title: Les yeux ne sont pas alignés
---

Si tu veux que les yeux soient alignés, assure-toi d'utiliser le même nombre pour les coordonnées des deux yeux. Essaie d'utiliser une variable pour que les valeurs soient toujours les mêmes.

--- /collapse ---

--- collapse ---

---
title: Je ne vois ni la pupille ni l'iris
---

L'œil doit d'abord être dessiné, puis l'iris et enfin la pupille. L'ordre dans lequel tu dessines les choses est très important.

L'infographie est composée de calques. Dans ton œil, chaque ellipse est un calque. Les objets des calques supérieurs se placent devant les objets des calques inférieurs. Imagine découper toutes les formes dans du papier. Selon la façon dont tu organises et superposes ce papier, le résultat final peut être très différent.

--- /collapse ---

--- collapse ---

---
title: Mes yeux ne sont pas ronds
---

Les troisième et quatrième nombres dans `ellipse` sont la largeur et la hauteur des yeux.

**Astuce :** si tu les fais identiques, tu obtiendras des yeux ronds.

--- /collapse ---


--- /task ---

--- save ---
