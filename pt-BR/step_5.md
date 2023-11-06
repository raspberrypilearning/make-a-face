## Adicione uma boca

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
A boca é uma ótima maneira de mostrar emoção. Seu personagem terá um sorriso, carranca ou outra coisa? 
</div>
<div>
![Imagem mostrando um rosto de robô como exemplo de rosto com boca.](images/mask.png){:width="200px"}
</div>
</div>

--- task ---

Pense em que tipo de boca seu rosto precisa. A boca mais simples seria um círculo para parecer surpreso.

Você pode adicionar dois círculos sobrepostos para criar um sorriso ou uma carranca. Triângulos ou retângulos podem ser adicionados para os dentes.

--- /task ---

--- task ---

Adicione o código à sua função `draw()` para adicionar uma boca.

--- collapse ---

---
título: Crie uma boca a partir de círculos sobrepostos
---

Defina a cor `fill` para sua boca e desenhe uma `elipse`. Defina a cor `fill` novamente, desta vez para combinar com a cor da face, depois desenhe uma segunda `elipse`.

Altere a coordenada `y` da segunda `elipse` para uma posição ligeiramente mais alta para um sorriso ou uma posição ligeiramente mais baixa para uma carranca.

![A área de saída mostrando uma boca sorridente.](images/smile.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # A black mouth
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0)  # An orange face
    ellipse(200, 235, 15, 15)  # Higher circle

--- /code ---

![A área de saída mostrando uma boca carrancuda.](images/frown.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # A black mouth
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0)  # An orange face
    ellipse(200, 245, 15, 15)  # Lower circle

--- /code ---

--- /collapse ---

--- collapse ---

---
título: Crie uma boca usando retângulos
---

Os robôs geralmente são mostrados com bocas em forma de `retângulo`. Às vezes, as formas `retângulo` e `elipse` são usadas juntas para criar um emoji de careta ou para adicionar uma máscara facial.

![A área de saída mostrando uma face com máscara retangular.](images/rectangle-mask.png)

Adicione o código para um `retângulo`e crie um `retângulo` menor dentro dele. Altere o `traço` e cores de `preenchimento` para complementar seu tema. Adicione formas de `elipse`, se necessário.

**Dica:** Lembre-se de colocar as formas de `elipses` acima do código do `retângulo` se quiser que elas fiquem atrás das formas `retangulares`.

--- code ---
---
language: python
filename: main.py - draw()
---

    # Face mask
    no_fill()
    stroke(255, 255, 255)
    ellipse(150, 250, 30, 30)  # Left ear loop
    ellipse(250, 250, 30, 30)  # Right ear loop
    fill(255, 255, 255)
    no_stroke()
    rect(150, 230, 100, 40)  # Large white rectangle
    fill(108, 200, 206)
    rect(152, 235, 96, 30)  # Smaller blue rectangle

--- /code ---

--- /collapse ---

**Tip:** Add a `#Mouth` comment on the line before your mouth code to help you easily find the mouth code.

--- /task ---

--- task ---

**Choose:** You could also add multiple teeth to your mouth using `translate` to change the `x` coordinate after each tooth is drawn.

--- collapse ---

---
título: Use um laço para adicionar uma fileira de dentes
---

Add code to create a `for` loop that repeats in order to create the number of teeth you need.

![The output area showing a robot face with a row of rectangle teeth in different colours.](images/robot-teeth.png)

After each tooth has been drawn, add code to `translate()` it by the width of the tooth.

You can also add code to change the colour of each tooth.

--- code ---
---
language: python
filename: main.py - draw()
---

    # Mouth
    fill(90, 110, 184)
    red = 90  # Starting amount of red
    green = 110  # Starting amount of green
    blue = 180  # Starting amount of blue
    for i in range (0,6):
        rect(100, 300, 33, 50)
        fill(red, green, blue)  # Uses variables to control the colour change each loop
        red = red+40
        blue = blue-30
        translate(33, 0)  # Move along the x coordinate by the width of a tooth


--- /code ---

--- /collapse ---

[[[processing-translation]]]

--- collapse ---

---
título: Use triângulos para adicionar presas
---

Create a `rectangle` to use as the line of the mouth.

Add two `triangle` shapes to create the fangs. Change the `x` coordinates for each corner to position the fangs at opposite ends of the mouth line.

![The output area showing a vampire face with a rectangle mouth and two triangle teeth.](images/vampire.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    # Mouth
    fill(0)
    rect(170, 260, 60, 5)  # Mouth line
    fill(0)
    triangle(170, 260, 180, 280, 190, 260)  # Left tooth
    triangle(210, 260, 220, 280, 230, 260)  # Right tooth
--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
título: Minha forma sobreposta sai do rosto
---

If you use two overlapping shapes to create a mouth, then you need to make sure the shape that is the same colour as the face doesn't go outside the face. If it does, then change the width or height of the shape so that it's small enough to fit inside the face.

--- /collapse ---


--- collapse ---

---
título: Eu tenho muitos dentes
---

Don't forget that `range()` creates a sequence of numbers starting from 0 not 1. This may make a difference to your code depending on how you have positioned your teeth.

--- /collapse ---

--- /task ---

--- save ---
