## Formato do rosto

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Desenhe e pinte uma forma para o seu rosto ou máscara. Não adicione os outros recursos ainda, eles virão mais tarde.
</div>
<div>
![Imagem de um robô de rosto quadrado.](images/robot-teeth.png){:width="200px"}
</div>
</div>

--- task ---

Decida o formato principal do rosto para sua máscara. Pode ser um círculo, uma elipse, um retângulo ou até mesmo um triângulo.

Adicione código à função `draw()` para desenhar um rosto ou máscara.

Este exemplo desenha um círculo preto no meio, mas cabe a você decidir qual forma e cor usar.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 10
line_highlights: 14, 15
---

def draw():
    # Coloque o código para executar em cada quadro aqui
    background(255, 255, 255)  # Mude para a cor de fundo

    # Adicione código para desenhar seu rosto aqui
    ellipse(width/2, height/2, 200, 200)  # Círculo no meio
    
    grid()  # adicione um # ao início desta linha para ocultar a grade

--- /code ---

![A área de saída mostrando um círculo preto no meio da grade.](images/black-circle.png)

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---

**Teste:** Execute seu código e altere-o para obter o tamanho e a forma do rosto que você deseja.

--- /task ---

--- task ---

Escolha uma cor de traçado para o contorno e uma cor de preenchimento para a parte principal da forma.

[[[processing-stroke]]]

Se você não quiser um contorno, use `no_stroke()`.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 13
line_highlights: 14
---

    # Adicione código para desenhar seu rosto aqui
    fill(255, 255, 0)  # Amarelo brilhante
    ellipse(largura/2, altura/2, 200, 200)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Teste:** Execute seu código e mude a cor até ficar satisfeito com ele.

--- /task ---

--- save ---
