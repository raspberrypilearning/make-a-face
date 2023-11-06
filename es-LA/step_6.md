## Agrega más detalles

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
¿Tu cara o máscara necesitan más detalles para hacerlos más interesantes? 
</div>
<div>
![Imagen que muestra un rostro como ejemplo con una diadema.](images/frida.png){:width="200px"}
</div>
</div>

--- task ---

Puedes usar más formas para agregar más características a tu cara o máscara.

¿Cómo puedes dar más personalidad a la cara?

Podrías agregar:

+ Una nariz
+ Cejas
+ Orejas
+ Mejillas
+ Reflejos o destellos
+ ¡Lo que quieras!

Simplemente agrega los detalles adicionales que tengan sentido para tu dibujo.

--- /task ---

--- task ---

Puedes hacer colores parcialmente transparentes agregando un cuarto número a un color RGB para dar **opacidad**.

Este código dibuja los reflejos superpuestos en el ejemplo de la fruta Kawaii:

--- code ---
---
language: python
filename: main.py - draw()
---

    # Highlights    
    fill(255, 255, 255, 70)  # 70 is transparency/opacity here    
    ellipse(170, 150, 35, 35)   
    ellipse(150, 160, 25, 25)

--- /code ---

![Imagen de fruta kawaii con reflejos en diferentes opacidades: 30, 70, 150, 255. El valor más bajo, 30, es más opaco y 255 es menos opaco.](images/opacity.png)

--- /task ---

--- save ---
