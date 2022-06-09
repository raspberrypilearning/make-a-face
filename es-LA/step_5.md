## Agrega una boca

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Una boca es una excelente manera de mostrar emociones. ¿Tu personaje tendrá una sonrisa, una mueca o algo más? 
</div>
<div>
![Imagen que muestra una cara de robot como ejemplo de una cara con boca.](images/mask.png){:width="200px"}
</div>
</div>

--- task ---

Piensa qué tipo de boca necesita tu rostro. La boca más simple sería un círculo, que expresa sorpresa.

Puedes agregar dos círculos superpuestos para crear una sonrisa o una mueca. Se pueden agregar triángulos o rectángulos para los dientes.

--- /task ---

--- task ---

Agrega código a la función `draw()` para dibujar una boca.

--- collapse ---

---
title: Crea una boca con círculos superpuestos
---

Establece el color de `relleno (fill)` para tu boca y luego dibuja una `elipse`. Establece el color de `relleno` nuevamente, esta vez para que coincida con el color de la cara, luego dibuja una segunda `elipse`.

Cambia la coordenada `y` de la segunda `elipse` a una posición ligeramente superior para una sonrisa o una posición ligeramente inferior para una mueca.

![El área de salida que muestra una boca sonriente.](images/smile.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0) #Una boca negra
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0) #Una cara naranja
    ellipse(200, 235, 15, 15) #Círculo superior

--- /code ---

![El área de salida que muestra una boca triste.](images/frown.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0) #Una boca negra
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0) #Una cara naranja
    ellipse(200, 245, 15, 15) #Círculo inferior

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Crea una boca usando rectángulos
---

Los robots a menudo se muestran con bocas en forma de `rectángulo`. A veces, las formas `rectángulo` y `elipse` se usan juntas para crear un emoji de mueca o para agregar una máscara.

![El área de salida que muestra una cara con una máscara rectangular.](images/rectangle-mask.png)

Agrega el código para un `rectángulo`, luego crea un `rectángulo` más pequeño dentro de éste. Cambia el `trazo` y los colores de `relleno` para complementar tu tema. Agrega fomas de `elipse` si es necesario.

**Sugerencia:** Recuerda colocar las `elipses`, arriba del código del `rectángulo` si quieres que vayan detrás de los `rectángulos`.

--- code ---
---
language: python
filename: main.py - draw()
---
#Máscara
no_fill()    
stroke(255, 255, 255)     
ellipse(150, 250, 30, 30) #Ciclo de la oreja izquierda    
ellipse(250, 250, 30, 30) #Ciclo de la oreja derecha    
fill(255, 255, 255)    
no_stroke()     
rect(150, 230, 100, 40) #Rectángulo blanco grande    
fill(108, 200, 206)    
rect(152, 235, 96, 30) #Rectángulo azul más pequeño

--- /code ---

--- /collapse ---

**Sugerencia:** Agrega un comentario `#Boca` en la línea antes del código de tu boca para ayudarte a encontrar fácilmente el código de la boca.

--- /task ---

--- task ---

**Elige:** También puedes agregar varios dientes a tu boca usando `translate` para cambiar la coordenada `x` después de dibujar cada diente.

--- collapse ---

---
title: Usa un ciclo para agregar una fila de dientes
---

Agrega código para crear un ciclo llamado `for` que se repite para crear la cantidad de dientes que necesitas.

![El área de salida que muestra una cara de robot con una fila de dientes rectangulares de diferentes colores.](images/robot-teeth.png)

Después de dibujar cada diente, agrega código para `translate()` el diente por el ancho de cada uno.

También puedes agregar código para cambiar el color de cada diente.

--- code ---
---
language: python
filename: main.py - draw()
---

#Boca
fill(90, 110, 184)     
  rojo = 90 #Cantidad inicial de rojo   
  verde = 110 #Cantidad inicial de verde    
  azul = 180 #Cantidad inicial de azul    
  for i in range (0,6):     
    rect(100, 300, 33, 50)     
    fill(rojo, verde, azul) #Utiliza variables para controlar el cambio de color de cada ciclo    
    rojo = rojo+40     
    azul = azul-30     
    translate(33, 0) #Cambia la coordenada x para cubrir el ancho de un diente


--- /code ---

--- /collapse ---

[[[processing-translation]]]

--- collapse ---

---
title: Usa triángulos para agregar colmillos
---

Crea un `rectángulo` para usarlo como la línea de la boca.

Agrega dos formas de `triángulo` para crear los colmillos. Cambia las coordenadas `x` para cada esquina para colocar los colmillos en los extremos opuestos de la línea de la boca.

![El área de salida muestra una cara de vampiro con una boca rectangular y dos dientes triangulares.](images/vampire.png)

--- code ---
---
language: python
filename: main.py - draw()
---
# Boca
  fill(0)    
  rect(170, 260, 60, 5) #Línea de la boca    
  fill(0)    
  triangle(170, 260, 180, 280, 190, 260) #Diente izquierdo    
  triangle(210, 260, 220, 280, 230, 260) #Diente derecho    
--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Depurar:** Es posible que encuentres algunos errores en tu proyecto que necesites corregir. A continuación, se muestran algunos errores comunes.

--- collapse ---

---
title: Mi forma superpuesta sale de la cara
---

Si usas dos formas superpuestas para crear una boca, debes asegurarte de que la forma que es del mismo color que la cara no salga de ésta. Si es así, cambia el ancho o la altura de la forma para que sea lo suficientemente pequeña como para caber dentro de la cara.

--- /collapse ---


--- collapse ---

---
title: Tengo demasiados dientes
---

No olvides que `range()` crea una secuencia de números a partir de 0, no de 1. Esto puede hacer la diferencia en tu código dependiendo de cómo hayas colocado tus dientes.

--- /collapse ---

--- /task ---

--- save ---
