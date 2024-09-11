--- question ---

---
legend: Pergunta 2 de 3
---

Em seu projeto, você adicionou código para desenhar um rosto com muitos recursos. A ordem do seu código foi extremamente importante para fazer o rosto parecer com o seu desenho.

Se você executasse esse código, como ficaria o rosto?

--- code ---
---
language: python

---

def draw():

  # Face
  stroke(0) # Preto
  fill(255) # Branco
  ellipse(200, 200, 200, 190)
  no_stroke()
  
  # Olhos
  fill(0, 255, 0) # Verde
  ellipse(160, 180, 60, 60)
  ellipse(240, 180, 60, 60)
  fill(0) # Preto
  ellipse(160, 180, 30, 30)
  ellipse(240, 180, 30, 30)
  
run()

--- /code ---

--- choices ---

- ( )

![Um rosto branco com contorno preto. Existem dois olhos verdes sólidos com contornos pretos.](images/face1.png)

 --- feedback ---

 Não é bem assim, observe a ordem das funções `ellipse()` e `stroke()`.

 --- /feedback ---

- ( )

![Um rosto branco com contorno preto. Existem dois olhos verdes com pupilas pretas e ambos têm um contorno preto.](images/face2.png)

 --- feedback ---

 Não é bem assim, veja a ordem das funções `stroke()`.

 --- /feedback ---

- (x)

![Um rosto branco com contorno preto. Existem dois olhos verdes com pupilas negras e os olhos não têm contorno.](images/face3.png)

 --- feedback ---

 Correto, o código desenha um rosto com um traço preto e desliga o traço antes de desenhar os círculos. Os círculos verdes são desenhados primeiro com os círculos pretos em cima deles.

 --- /feedback ---

- ( )

![Um rosto branco com contorno preto. Existem dois olhos verdes sólidos que não têm contorno.](images/face4.png)

 --- feedback ---

 Não é bem assim, veja a ordem das funções `ellipse()`.

 --- /feedback ---

--- /choices ---

--- /question ---
