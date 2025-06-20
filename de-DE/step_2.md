## Wähle eine Hintergrundfarbe

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Hast du eine Vorstellung davon, was für ein Gesicht oder welche Maske du machen möchtest? Verwende diesen Schritt, um deine Kunst zu planen und deine Leinwand einzurichten.
</div>
<div>
![Der Ausgabebereich mit einem Vampirgesicht.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Öffne das [-Starterprojekt](https://editor.raspberrypi.org/de-DE/projects/make-face-starter){:target="_blank"}.

--- /task ---

--- task ---

Die drei Zahlen in `background(0, 0, 0)` sind Werte für Rot, Grün und Blau. Experimentiere und ändere die Zahlen auf beliebige ganze Zahlen zwischen 0 und 255, um die Hintergrundfarbe zu ändern.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 14
---
 
def draw():   
    # Füge hier den Code ein, der bei jedem Frame ausgeführt werden soll
    background(0, 0, 0)    
  
--- /code ---

--- /task ---

--- task ---

**Test:** Führe deinen Code aus und du solltest ein farbiges Quadrat als Hintergrund sehen.

--- /task ---
