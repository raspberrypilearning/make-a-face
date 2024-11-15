## Choose a background colour

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Você tem uma ideia sobre o tipo de rosto ou máscara que deseja fazer? Use esta etapa para planejar sua arte e configurar sua tela.
</div>
<div>
![A área de saída com um rosto com tema de vampiro.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Open the [starter project](https://editor.raspberrypi.org/en/projects/make-face-starter){:target="_blank"}.

--- /task ---

--- task --- The three numbers in `background(0, 0, 0)` are red, green and blue values. Experiment with changing the numbers to any whole number between 0 and 255 to change the background colour.

--- code ---
---
language: python line_numbers: true line_number_start: 12
line_highlights: 14
---

def draw():   
# Put code to run every frame here background(0, 0, 0)

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and you should see a coloured square as your background.

--- /task ---
