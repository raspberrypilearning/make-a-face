## Kies een achtergrondkleur

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Heb je een idee over het soort gezicht of masker dat je wilt maken? Gebruik deze stap om een plannetje te maken voor je kunstwerk en je canvas in te stellen.
</div>
<div>
![Het outputgebied met een gezicht met een vampierthema.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Open het [startproject](https://editor.raspberrypi.org/en/projects/make-face-starter){:target="_blank"}.

--- /task ---

--- task ---

De drie getallen in `background(0, 0, 0)` zijn de rode, groene en blauwe waarden. Experimenteer met het veranderen van de getallen in een geheel getal tussen 0 en 255 om de achtergrondkleur te veranderen.

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

**Test:** Voer je code uit en je zou een gekleurd vierkant moeten zien als je achtergrond.

--- /task ---
