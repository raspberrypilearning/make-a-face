## Escolha um tema

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Você tem uma ideia sobre o tipo de rosto ou máscara que deseja fazer? Use esta etapa para planejar sua arte e configurar sua tela.
</div>
<div>
![A área de saída com um rosto com tema de vampiro.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Abra o [projeto inicial](https://editor.raspberrypi.org/pt-BR/projects/make-face-starter){:target="_blank"}. O editor de código Raspberry Pi será aberto em outra guia do navegador.

--- /task ---

--- task ---

**Escolha:** Pense no tipo de rosto que deseja fazer:
+ Você quer escolher algo de sua herança ou cultura popular?
+ Sua arte mostrará um ser humano, animal, algo mítico ou talvez uma máquina?
+ Você pode até querer criar um autorretrato!
+ Você pode desenhar um emoji para compartilhar com seus amigos

--- /task ---

--- task ---

A primeira coisa a fazer ao criar arte usando a `Biblioteca de processamento` Python é adicionar `def setup():` para definir uma função `setup` que é executada uma vez no início do seu programa.

O projeto inicial tem uma função `setup` que define o `tamanho` da sua tela para `400` largura e `400` de altura.

**Escolha:** Experimente os números e execute seu código para encontrar um tamanho que lhe agrade.

--- collapse ---

---
title: Configurando o tamanho da tela quando seu programa inicia
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
    size(400, 400)  # 400 por 400 funciona bem para um rosto redondo

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Escolha:** Pense nas cores que você usará para o seu rosto e altere os valores das cores de `fundo` para definir sua tela com uma cor complementar.

[[[generic-theory-simple-colours]]]

--- collapse ---

---
title: Definindo a cor de fundo quando seu programa inicia
---

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 9
line_highlights: 9
---
    background(255, 255, 255)  # Tente números diferentes para mudar a cor

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Dica:** A função `draw` tem código `grid()`. Isso adiciona uma grade de coordenadas sobre o plano de fundo que ajuda você a descobrir onde posicionar características em seu rosto.

Para desativar a grade, adicione um `#` na frente do código, para ativá-la novamente, remova o `#`.

--- code ---
---
language: python
filename: main.py - draw()
---
    grid()  # Mostra a grade

--- /code ---

--- code ---
---
language: python
filename: main.py - draw()
---
    #grid()  # Oculte a grade transformando-a em um comentário

--- /code ---

--- /task ---

--- task ---

**Teste:** Execute seu projeto para ver o tamanho de tela e a cor de fundo escolhidos.

--- /task ---

--- task ---

**Depurar:** Você pode encontrar alguns erros em seu projeto que precisa corrigir. Aqui estão alguns erros comuns.

--- collapse ---

---
title: Atualizei o tamanho e cor, mas a janela do programa permanece a mesma
---

Depois de alterar o código, você precisará **`Executar`** seu projeto para ver as alterações na área de saída.

--- /collapse ---

--- collapse ---

---
título: Eu tentei diferentes números, mas a cor de fundo não se altera
---

O valor máximo de vermelho, verde ou azul é `255`. Tenha certeza de que todos os valores de cor de `fundo` estejam entre `0` e `255`.

--- /collapse ---

--- /task ---

--- save ---
