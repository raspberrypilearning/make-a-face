## Adicione olhos

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Os olhos fazem uma forma começar a se parecer com um rosto.
</div>
<div>
![A área de saída mostrando um rosto com olhos.](images/eyes.png){:width="200px"}
</div>
</div>

--- task ---

Pense em que tipo de olhos seu rosto precisa. Os olhos mais simples são apenas dois círculos.

Você pode adicionar íris e pupilas de cores diferentes. Você pode adicionar realces de luz / holofotes em uma cor diferente.

--- /task ---

Experimente com `elipses` na função `draw` para criar os olhos que você deseja.

--- task ---

### Posicione os olhos

O primeiro número na função `ellipse` é o centro do olho. Os olhos devem estar posicionados à mesma distância do centro do desenho.

Neste exemplo, `160` e `240` estão ambos `40` píxeis de distância de 200, o que funciona para um desenho com uma largura de 400.

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Black — change to red, green, or blue up to 255
    eye_size = 50
    ellipse(160, 180, eye_size, eye_size)  # x, y, width, height
    ellipse(240, 180, eye_size, eye_size)

--- /code ---

**Dica:** Se você quiser olhos redondos, usar uma variável `eye_size` facilita alterar a largura e a altura de ambos os olhos em um só lugar.

[[[processing-python-ellipse]]]

--- collapse ---

---
title: Calculando posições com base na largura
---

O centro de um desenho está na posição `largura / 2` ou metade da largura. Você pode usar isso para posicionar os olhos subtraindo a largura do olho para o olho esquerdo e adicionando-a para o olho direito:

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Black — change to red, green, or blue up to 255
    eye_size = 50
    ellipse( (width / 2) - 40, 180, eye_size, eye_size)  # x, y, width, height
    ellipse( (width / 2) + 40 , 180, eye_size, eye_size)

--- /code ---

Você também pode calcular a largura dos olhos com base na largura do desenho.

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Black — change to red, green, or blue up to 255
    ellipse( (width / 2) - (width / 10) , 180, eye_size, eye_size)  # x, y, width, height
    ellipse( (width / 2) + (width / 10) , 180, eye_size, eye_size)

--- /code ---

--- /collapse ---

Altere o segundo número na chamada da `ellipse` para mover a posição `y` (vertical) dos olhos.

--- /task ---

--- task ---

**Teste:** Continue mudando a forma e a posição dos olhos até gostar da aparência deles.

**Dica:** Se você definir um traço para desenhar o rosto e não quiser um para os olhos, precisará chamar `no_stroke()` antes de desenhar os olhos.

[[[processing-stroke]]]

--- /task ---

--- task ---

### Adicione detalhes

Você pode usar mais círculos para criar:
+ Íris coloridas
+ Pupilas negras
+ Holofotes brancos
+ Ou alguma outra coisa

Este olho tem uma íris colorida, pupila preta e holofotes brancos com opacidade alterada: ![A área de saída mostrando um olho com holofotes sobre a pupila e a íris.](images/catchlights.png)

\[[[generic-theory-simple-colours]]\] \[[[processing-opacity\]]]

Você também pode animar os olhos girando-os.

[[[processing-rotation]]]

--- /task ---

--- task ---

**Teste:** Continue mudando os olhos até gostar da aparência deles.

Seu desenho está começando a se parecer a um rosto?

--- /task ---

--- task ---

**Debug:** Talvez você encontre alguns bugs em seu projeto que precisem de correção. Aqui estão alguns bugs comuns.

--- collapse ---
---
título: Os olhos não estão centrados
---

Você pode usar `height / 2` para colocá-los no centro.

--- /collapse ---

--- collapse ---
---
título: Os olhos não estão alinhados entre si
---

Se quiser que os olhos fiquem alinhados, certifique-se de usar o mesmo número para as coordenadas de ambos os olhos. Tente usar uma variável para que os valores sejam sempre os mesmos.

--- /collapse ---

--- collapse ---

---
título: Não consigo ver a pupila ou a íris
---

O olho precisa ser desenhado primeiro, depois a íris e, finalmente, a pupila. A ordem em que você desenhar as coisas é muito importante.

Gráficos de computadores são feitos de camadas. Em seu olho, cada elipse é uma camada. Objetos em camadas superiores ficam na frente de objetos em camadas inferiores. Imagine recortar formas de papel. Dependendo de como você posiciona e sobrepõe esse papel, o resultado pode ser muito diferente.

--- /collapse ---

--- collapse ---

---
título: Meus olhos não são redondos
---

O terceiro e quarto números em `ellipse` são a largura e a altura dos olhos.

**Dica:** Se você os fizer iguais, terá olhos redondos.

--- /collapse ---


--- /task ---

--- save ---
