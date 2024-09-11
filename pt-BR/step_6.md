## Adicione mais detalhes

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Seu rosto ou máscara precisa de mais detalhes para torná-lo mais interessante? 
</div>
<div>
![Imagem mostrando um rosto como exemplo com um acessório de bandana.](images/frida.png){:width="200px"}
</div>
</div>

--- task ---

Você pode usar mais formas para adicionar mais características ao seu rosto ou máscara.

Como dar mais personalidade ao rosto?

Você poderia adicionar:

+ Um nariz
+ Sobrancelhas
+ Ouvidos
+ Bochechas
+ Realces / holofotes
+ O que você quiser!

Basta adicionar os detalhes extras que fazem sentido para o seu desenho.

--- /task ---

--- task ---

Você pode criar cores parcialmente transparentes adicionando um quarto número a uma cor RGB para fornecer a **opacidade**.

Este código desenha os realces sobrepostos com o exemplo da fruta Kawaii:

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

![Imagem da fruta Kawaii com realce em diferentes opacidades: 30, 70, 150, 255. O valor mais baixo, 30, é menos opaco e 255 é mais opaco.](images/opacity.png)

--- /task ---

--- save ---
