## Ajouter plus de détails

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ton visage ou ton masque a-t-il besoin de plus de détails pour le rendre plus intéressant ? 
</div>
<div>
![Image montrant un visage à titre d'exemple avec un accessoire bandeau.](images/frida.png){:width="200px"}
</div>
</div>

--- task ---

Tu peux utiliser plus de formes pour ajouter plus de fonctionnalités à ton visage ou à ton masque.

Comment donner plus de personnalité au visage ?

Tu pourrais ajouter :

+ Un nez
+ Des sourcils
+ Des oreilles
+ Des joues
+ Reliefs / reflets
+ Tout ce que tu aimes !

Ajoute simplement les détails supplémentaires qui ont du sens pour ton dessin.

--- /task ---

--- task ---

Tu peux créer des couleurs partiellement transparentes en ajoutant un quatrième chiffre à une couleur RVB pour donner **l'opacité**.

Ce code dessine les reflets qui se chevauchent dans l'exemple de fruit Kawaii :

--- code ---
---
language: python
filename: main.py - draw()
---

    #Zones claires<br x-id="3" />
      fill(255, 255, 255, 70) #70 est la transparence/opacité ici<br x-id="4" />
      ellipse(170, 150, 35, 35)<br x-id="3" />
      ellipse(150, 160, 25, 25)

--- /code ---

![Image de fruits kawaii avec des reflets à différentes opacités : 30, 70, 150, 255. La valeur inférieure, 30, est plus opaque et 255 est moins opaque.](images/opacity.png)

--- /task ---

--- save ---
