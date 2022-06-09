## Elige un tema

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
¿Tienes alguna idea sobre el tipo de cara o máscara que quieres hacer? Usa este paso para planificar tu arte y configurar tu lienzo.
</div>
<div>
![El área de salida con una cara tipo vampiro.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Abre el [proyecto inicial](https://trinket.io/library/trinkets/a68341f248){:target="_blank"}. Trinket se abrirá en otra pestaña del navegador.

--- /task ---

--- task ---

**Elige:** Piensa en el tipo de cara que quieres hacer:
+ ¿Quieres elegir algo de tu propia tradición o cultura popular?
+ ¿Tu arte mostrará un ser humano, un animal, algo mítico o quizás una máquina?
+ ¡Incluso podrías crear un autorretrato!
+ Podrías dibujar un emoji para compartir con tus amigos

--- /task ---

--- task ---

Lo primero que debes hacer al crear arte utilizando la `biblioteca de procesamiento` de Python es agregar `def setup():` para definir una función `setup` que se ejecuta una vez al comienzo de tu programa.

El proyecto inicial tiene una función `setup` que establece el `tamaño` de tu lienzo en `400` de ancho y `400` de alto.

**Elige:** Experimenta con los números y ejecuta tu código para encontrar el tamaño que más te guste.

--- collapse ---

---
title: Configurar el tamaño de la pantalla cuando se inicia el programa
---

--- code ---
---
language: python 
filename: main.py - setup() 
line_numbers: true 
line_number_start: 6
line_highlights: 7
---
def setup():   
    size(400, 400) #400 por 400 funciona bien para una cara redonda

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Elige:** Piensa en los colores que usarás para la cara y cambia los valores de color del `fondo` para configurar tu pantalla con un color complementario.

[[[generic-theory-simple-colours]]]

--- collapse ---

---
title: Configurar el color de fondo cuando se inicia el programa
---

--- code ---
---
language: python 
filename: main.py - draw() 
line_numbers: true 
line_number_start: 9
line_highlights: 9
---

    background(255, 255, 255) #Prueba diferentes números para cambiar el color

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Sugerencia:** La función `draw` tiene el código `grid()`. Esto agrega una cuadrícula de coordenadas sobre tu fondo que te ayuda a determinar dónde colocar las características en tu cara.

Para quitar la cuadrícula, agrega un `#` delante del código, para volver a ponerla, elimina el `#`.

--- code ---
---
language: python
filename: main.py - draw()
---

    grid() #Muestra cuadrícula

--- /code ---

--- code ---
---
language: python
filename: main.py - draw()
---

    #grid() #Oculta la cuadrícula convirtiéndola en un comentario

--- /code ---

--- /task ---

--- task ---

**Prueba:** Ejecuta tu proyecto para ver el tamaño de pantalla y el color de fondo elegidos.

--- /task ---


--- task ---

**Depurar:** Es posible que encuentres algunos errores en tu proyecto que necesites corregir. A continuación, se muestran algunos errores comunes.

--- collapse ---

---
title: Actualicé el tamaño y el color, pero el resultado permanece igual
---

Después de cambiar el código, deberás `ejecutar (run)` tu proyecto para poder visualizar los cambios.

--- /collapse ---

--- collapse ---

---
title: Probé con diferentes números, pero el color de fondo no cambia
---

La cantidad máxima de rojo, verde o azul es `255`. Asegúrate de que todos los valores de `fondo (background)` estén entre `0` y `255`.

--- /collapse ---

--- /task ---

--- save ---
