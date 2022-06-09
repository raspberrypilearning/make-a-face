--- question ---

---
legend: Pregunta 2 de 3
---

En tu proyecto, agregaste código para dibujar una cara con muchas características. El orden de tu código fue extremadamente importante para que la cara se pareciera a tu diseño.

Si ejecutaras este código, ¿cómo se vería la cara?

--- code ---
---
language: python

---

def draw():

  #Face stroke(0) #Black fill(255) #White ellipse(200, 200, 200, 190) no_stroke()

  #Eyes fill(0, 255, 0) #Green ellipse(160, 180, 60, 60) ellipse(240, 180, 60, 60) fill(0) #Black ellipse(160, 180, 30, 30) ellipse(240, 180, 30, 30)

run()

--- /code ---

--- choices ---

- ( )

![Una cara blanca con contorno negro. Hay dos ojos verdes sólidos con contornos negros.](images/face1.png)

 --- feedback ---

 No precisamente, observa el orden de las funciones `ellipse()` y `stroke()`.

 --- /feedback ---

- ( )

![Una cara blanca con contorno negro. Hay dos ojos verdes con pupilas negras y ambos tienen un contorno negro.](images/face2.png)

 --- feedback ---

 No precisamente, mira el orden de las funciones `stroke()`.

 --- /feedback ---

- (x)

![Una cara blanca con contorno negro. Hay dos ojos verdes con pupilas negras y los ojos no tienen contorno.](images/face3.png)

 --- feedback ---

 Correcto, el código dibuja una cara con un contorno negro y luego quita el contorno antes de dibujar los círculos. Los círculos verdes están dibujados primero con los círculos negros sobre éstos.

 --- /feedback ---

- ( )

![Una cara blanca con contorno negro. Hay dos ojos de color verde sólido que no tienen contorno.](images/face4.png)

 --- feedback ---

 No precisamente, mira el orden de las funciones `ellipse()`.

 --- /feedback ---

--- /choices ---

--- /question ---
