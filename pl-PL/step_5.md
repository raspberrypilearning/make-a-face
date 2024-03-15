## Dodaj usta

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Usta to świetny sposób na pokazanie emocji. Czy Twoja postać będzie miała uśmiech, zmarszczkę lub coś innego? 
</div>
<div>
![Obraz przedstawiający twarz robota jako przykład twarzy z ustami.](images/mask.png){:width="200px"}
</div>
</div>

--- task ---

Zastanów się, jakiego rodzaju usta potrzebuje twoja twarz. Najprostsze usta byłyby kółkiem, który wygląda na zaskoczonego.

Możesz dodać dwa nakładające się koła, aby stworzyć uśmiech lub zmarszczkę. Dla zębów można dodać trójkąty lub prostokąty.

--- /task ---

--- task ---

Dodaj kod do funkcji ` draw()`, aby dodać usta.

--- collapse ---

---
Title: Utwórz usta z nakładających się okręgów
---

Ustaw kolor ` fill ` dla ust, a następnie narysuj ` elipsesa `. Ponownie ustaw kolor ` `, tym razem tak, aby pasował do koloru twarzy, a następnie narysuj drugą ` elipsesę `.

Zmień współrzędną `.` drugiej elipsy ` ` na nieco wyższą pozycję, aby uzyskać uśmiech lub nieco niższą pozycję dla zmarszczek.

![Obszar wyjściowy pokazujący uśmiechnięte usta.](images/smile.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # A black mouth
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0)  # An orange face
    ellipse(200, 235, 15, 15)  # Higher circle

--- /code ---

![Obszar wyjściowy pokazujący zmarszczki w ustach.](images/frown.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # A black mouth
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0)  # An orange face
    ellipse(200, 245, 15, 15)  # Lower circle

--- /code ---

--- /collapse ---

--- collapse ---

---
Title: Utwórz usta używając prostokątów
---

Roboty są często pokazywane z ustami w kształcie prostokąta ` w kształcie `. Czasami kształty ` prostokąty ` i ` elipsy ` są używane razem, aby utworzyć emoji grymasu lub dodać maskę twarzy.

![Obszar wyjściowy pokazujący ścianę z prostokątną maską twarzy.](images/rectangle-mask.png)

Dodaj kod dla prostokąta ` `, a następnie utwórz w nim mniejszy prostokąt ` prostokątny `. Zmień kolory ` ` i ` `, aby uzupełnić swój motyw. W razie potrzeby dodaj kształty ` elipse `.

** Wskazówka:** Pamiętaj, aby umieścić kształty ` elipsy ` nad kodem ` prostokątny `, jeśli chcesz, aby były one za kształtami ` prostokątne `.

--- code ---
---
language: python
filename: main.py - draw()
---

    # Face mask
    no_fill()
    stroke(255, 255, 255)
    ellipse(150, 250, 30, 30)  # Left ear loop
    ellipse(250, 250, 30, 30)  # Right ear loop
    fill(255, 255, 255)
    no_stroke()
    rect(150, 230, 100, 40)  # Large white rectangle
    fill(108, 200, 206)
    rect(152, 235, 96, 30)  # Smaller blue rectangle

--- /code ---

--- /collapse ---

** Wskazówka:** Dodaj komentarz `#` na linii przed kodem ust, aby pomóc Ci łatwo znaleźć kod ust.

--- /task ---

--- task ---

** Wybierz:** Możesz również dodać wiele zębów do ust za pomocą ` translate `, aby zmienić współrzędną ` ` po narysowaniu każdego zęba.

--- collapse ---

---
Title: Użyj pętli, aby dodać rząd zębów
---

Dodaj kod, aby utworzyć pętlę ` `, która powtarza się w celu utworzenia potrzebnej liczby zębów.

![Obszar wyjściowy przedstawiający twarz robota z rzędem prostokątnych zębów w różnych kolorach.](images/robot-teeth.png)

Po narysowaniu każdego zęba dodaj kod do ` translate()` go o szerokość zęba.

Możesz również dodać kod, aby zmienić kolor każdego zęba.

--- code ---
---
language: python
filename: main.py - draw()
---

    # Mouth
    fill(90, 110, 184)
    red = 90  # Starting amount of red
    green = 110  # Starting amount of green
    blue = 180  # Starting amount of blue
    for i in range (0,6):
        rect(100, 300, 33, 50)
        fill(red, green, blue)  # Uses variables to control the colour change each loop
        red = red+40
        blue = blue-30
        translate(33, 0)  # Move along the x coordinate by the width of a tooth


--- /code ---

--- /collapse ---

[[[processing-translation]]]

--- collapse ---

---
Title: Użyj trójkątów, aby dodać kły
---

Utwórz prostokątny ` `, który będzie używany jako linia ust.

Dodaj dwa kształty ` trójkątne `, aby utworzyć kły. Zmień współrzędne ` ` dla każdego rogu, aby ustawić kły na przeciwnych końcach linii ust.

![Obszar wyjściowy przedstawiający twarz wampira z prostokątnymi ustami i dwoma trójkątnymi zębami.](images/vampire.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    # Mouth
    fill(0)
    rect(170, 260, 60, 5)  # Mouth line
    fill(0)
    triangle(170, 260, 180, 280, 190, 260)  # Left tooth
    triangle(210, 260, 220, 280, 230, 260)  # Right tooth
--- /code ---

--- /collapse ---

--- /task ---

--- task ---

** Debug:** Możesz znaleźć kilka błędów w swoim projekcie, które musisz naprawić. Oto kilka typowych robaków.

--- collapse ---

---
Title: Mój zachodzący kształt wychodzi poza ścianę
---

Jeśli użyjesz dwóch nakładających się kształtów, aby utworzyć usta, musisz upewnić się, że kształt, który jest tego samego koloru co ściana, nie wychodzi na zewnątrz ściany. Jeśli tak, zmień szerokość lub wysokość kształtu tak, aby był wystarczająco mały, aby zmieścił się wewnątrz ściany.

--- /collapse ---


--- collapse ---

---
Title: Mam za dużo zębów
---

Nie zapominaj, że ` range()` tworzy sekwencję liczb zaczynającą się od 0 a nie 1. Może to zmienić twój kod w zależności od tego, jak ustawiłeś swoje zęby.

--- /collapse ---

--- /task ---

--- save ---
