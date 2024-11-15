## Choose a background colour

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Ти вже маєш уявлення про те, яке обличчя або маску ти хочеш створити? Скористайся цим етапом, щоб спланувати свою роботу та підготувати полотно.
</div>
<div>
![Область виводу з обличчям на вампірську тематику.](images/vampire.png){:width="200px"}
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
