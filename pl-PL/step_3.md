## Kształt ściany

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Narysuj i pokoloruj kształt twarzy lub maski. Nie dodawaj jeszcze innych funkcji, pojawią się później.
</div>
<div>
![Obraz robota o kwadratowej powierzchni.](images/robot-teeth.png){:width="200px"}
</div>
</div>

--- task ---

Zdecyduj o głównym kształcie twarzy dla swojej maski. Może to być okrąg, elipsa, prostokąt, a nawet trójkąt.

Dodaj kod do funkcji ` draw()`, aby narysować twarz lub maskę.

Ten przykład rysuje na środku czarny okrąg, ale to od Ciebie zależy, jaki kształt i kolor ma użyć.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 10
line_highlights: 14, 15
---

def draw(): # Put code to run every frame here background(255, 255, 255)  # Change to your background colour

    # Add code to draw your face here
    ellipse(width/2, height/2, 200, 200)  # Circle in the middle
    
    grid()  # add a # to the beginning of this line to hide the grid

--- /code ---

![Obszar wyjściowy pokazujący koło czarnej linii na środku siatki.](images/black-circle.png)

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---

Test **:** Uruchom swój kod i zmień go, aby uzyskać żądany rozmiar i kształt twarzy.

--- /task ---

--- task ---

Wybierz kolor obrysu i kolor wypełnienia dla głównej części kształtu.

[[[processing-stroke]]]

Jeśli nie chcesz konturu, użyj ` no_stroke()`.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 13
line_highlights: 14
---

    # Add code to draw your face here
    fill(255, 255, 0)  # Bright yellow
    ellipse(width/2, height/2, 200, 200)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

Test **:** Uruchom swój kod i zmieniaj kolor, aż będziesz z niego zadowolony.

--- /task ---

--- save ---
