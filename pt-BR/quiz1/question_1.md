## Teste rápido

Responda às três perguntas. Existem dicas para guiá-lo para a resposta correta.

Após responder cada pergunta, clique em **Verificar minha resposta**.

Divirta-se!

Divirta-se!

--- question ---

---
legend: Pergunta 1 de 3
---

No seu projeto, você desenhou bocas usando formas.

Que tipo de boca esse código desenharia?

--- code ---
---
language: python

---
def draw():
  fill(0, 0, 0) # Preto
  ellipse(160, 200, 150, 150)
  fill(255, 255, 255) # Branco
  ellipse(160, 150, 150, 150)

--- /code ---

--- choices ---

- ( ) ![](images/sad-mouth.png)

  --- feedback ---

  Não é bem assim, para criar uma boca triste, a segunda `elipse` precisaria de uma **coordenada_y** que é menor que a primeira `elipse`.

  --- /feedback ---

- (x) ![](images/happy-mouth.png)

  --- feedback ---

  Está correto! A segunda `elipse` é desenhada com uma **coordenada_y** que é mais alta que a primeira `elipse`.

  --- /feedback ---

- () ![](images/circle-mouth.png)

  --- feedback ---

   Não é bem assim, o segundo círculo tem um preenchimento branco `fill(255, 255, 255)` e está posicionado parcialmente sobre o primeiro círculo preto.

  --- /feedback ---

- ( ) ![](images/square-mouth.png)

  --- feedback ---

O código não desenha retângulos. A função `ellipse` desenha círculos.

  --- /feedback ---

--- /choices ---

--- /question ---
