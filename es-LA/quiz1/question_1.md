## Reflexión

¡Bien hecho, has aprendido mucho! Ahora es momento de reflexionar: esta es una parte importante del aprendizaje porque te ayuda a establecer nuevas conexiones en tu cerebro.

Responde las siguientes tres preguntas para reflexionar sobre lo que has aprendido.

Después de cada pregunta, presiona **enviar**. Vamos a guiarte hacia la respuesta correcta. Puedes realizar esta actividad tantas veces como quieras.

¡Que te diviertas!

--- question ---

---
legend: Pregunta 1 de 3
---

En tu proyecto, dibujaste bocas usando formas.

¿Qué tipo de boca dibujaría este código?

--- code ---
---
language: python

---
def draw():
  fill(0, 0, 0) #Negro
  ellipse(160, 200, 150, 150)
  fill(255, 255, 255) #Blanco
  ellipse(160, 150, 150, 150)

--- /code ---

--- choices ---

- ( ) ![](images/sad-mouth.png)

  --- feedback ---

  No precisamente, para crear una boca triste, la segunda `elipse`, necesitaría una **y_coordinada** más baja que la primera `elipse`.

  --- /feedback ---

- (x) ![](images/happy-mouth.png)

  --- feedback ---

  ¡Correcto! La segunda `elipse` se dibuja con una **y_coordinada** más alta que la primera `elipse`.

  --- /feedback ---

- () ![](images/circle-mouth.png)

  --- feedback ---

   No exactamente, el segundo círculo tiene un relleno blanco, `fill(255, 255, 255)`, y está colocado parcialmente sobre el primer círculo negro.

  --- /feedback ---

- ( ) ![](images/square-mouth.png)

  --- feedback ---

El código no dibuja rectángulos. La función `ellipse` dibuja círculos.

  --- /feedback ---

--- /choices ---

--- /question ---
