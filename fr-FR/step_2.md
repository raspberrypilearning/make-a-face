## Choisir un thème

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
As-tu une idée du type de visage ou de masque que tu souhaites réaliser ? Utilise cette étape pour planifier ton art et configurer ta zone de travail.
</div>
<div>
![La zone de sortie avec un visage sur le thème des vampires.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Ouvre le [projet de démarrage](https://trinket.io/library/trinkets/54d15b9cdf){:target="_blank"}. Trinket s'ouvrira dans un autre onglet du navigateur.

--- /task ---

--- task ---

**Choisir :** Réfléchis au type de visage que tu veux faire :
+ Veux-tu choisir quelque chose de ton héritage ou de ta culture populaire ?
+ Ton art montrera-t-il un humain, un animal, quelque chose de mythique ou peut-être une machine ?
+ Tu voudras peut-être même créer un autoportrait !
+ Tu pourrais dessiner un emoji à partager avec tes amis

--- /task ---

--- task ---

La première chose à faire lors de la création artistique à l'aide de la bibliothèque Python `Processing` est d'ajouter `def configuration():` pour définir une fonction `configuration` qui est exécutée une fois au début de ton programme.

Le projet de démarrage a une fonction `configuration` qui définit la `taille` de ta zone de travail à `400` de largeur et `400` de hauteur.

**Choisir :** Expérimente avec les nombres et exécute ton code pour trouver une taille qui te convient.

--- collapse ---

---
title: Définir la taille de l'écran au démarrage de ton programme
---

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 7
---
def setup():   
size(400, 400) #400 by 400 works well for a round face

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Choisir :** Pense aux couleurs que tu utiliseras pour ton visage et change les couleurs `d'arrière-plan` pour régler ton écran sur une couleur complémentaire.

[[[generic-theory-simple-colours]]]

--- collapse ---

---
title: Définir la couleur d'arrière-plan au démarrage de ton programme
---

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 9
line_highlights: 9
---

    background(255, 255, 255) #Try different numbers to change the colour

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Astuce :** La fonction `dessiner` a un code `grid()`. Cela ajoute une grille de coordonnées sur ton arrière-plan qui t'aide à déterminer où positionner les traits sur ton visage.

Pour désactiver la grille, ajoute un `#` devant le code, pour la réactiver, supprime le `#`.

--- code ---
---
language: python
filename: main.py - draw()
---

    grid() #Shows grid

--- /code ---

--- code ---
---
language: python
filename: main.py - draw()
---

    #grid() #Hide grid by turning it into a comment

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton projet pour voir la taille d'écran et la couleur d'arrière-plan que tu as choisies.

--- /task ---


--- task ---

**Débogage :** Il est possible que tu trouves des bogues dans ton projet que tu dois corriger. Voici quelques bogues assez courants.

--- collapse ---

---
title : J'ai mis à jour ma taille et ma couleur mais la zone de sortie reste la même
---

Après avoir modifié le code, tu devras `exécuter` ton projet pour voir les changements dans la zone de sortie.

--- /collapse ---

--- collapse ---

---
title: J'ai essayé différents numéros, mais la couleur d'arrière-plan ne change pas
---

La quantité maximale de rouge, de vert ou de bleu est de `255`. Assure-toi que toutes tes valeurs de couleur `d'arrière-plan` sont comprises entre `0` et `255`.

--- /collapse ---

--- /task ---

--- save ---
