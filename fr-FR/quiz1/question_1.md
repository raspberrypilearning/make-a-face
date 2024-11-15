## Questionnaire rapide

Réponds aux trois questions. Il y a des indices pour te guider vers la bonne réponse.

Lorsque tu as répondu à chaque question, clique sur **Vérifier ma réponse**.

Amuse-toi bien !

--- question ---

---
legend: Question 1 sur 3
---

Dans ton projet, tu as dessiné des bouches à l'aide de formes.

Quel genre de bouche ce code dessinerait-il ?

--- code ---
---
language: python

---
def draw(): fill(0, 0, 0) #Black ellipse(160, 200, 150, 150) fill(255, 255, 255) #White ellipse(160, 150, 150, 150)

--- /code ---

--- choices ---

- ( ) ![](images/sad-mouth.png)

  --- feedback ---

  Pas tout à fait, pour créer une bouche triste, la deuxième `ellipse` doit avoir une **coordonnee_y** inférieure à celle de la première `ellipse`.

  --- /feedback ---

- (x) ![](images/happy-mouth.png)

  --- feedback ---

  C'est correct ! La seconde `ellipse` est dessinée avec une **coordonnee_y** supérieure à la première `ellipse`.

  --- /feedback ---

- () ![](images/circle-mouth.png)

  --- feedback ---

   Pas tout à fait, le deuxième cercle a un `fill(255, 255, 255) blanc` et est positionné partiellement sur le premier cercle noir.

  --- /feedback ---

- ( ) ![](images/square-mouth.png)

  --- feedback ---

Le code ne dessine pas de rectangles. La fonction `ellipse` dessine des cercles.

  --- /feedback ---

--- /choices ---

--- /question ---
