## Dodaj oczy

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Oczy sprawiają, że kształt zaczyna wyglądać jak twarz.
</div>
<div>
![Obszar wyjściowy pokazujący twarz z oczami.](images/eyes.png){:width="200px"}
</div>
</div>

--- task ---

Zastanów się, jakich oczu potrzebuje twoja twarz. Najprostsze oczy to tylko dwa koła.

Możesz dodać różne kolorowe tęczówki i źrenice. Możesz dodać podświetlenia / podświetlenia w innym kolorze.

--- /task ---

Eksperymentuj z ` ` w funkcji ` rysowanie `, aby stworzyć żądane oczy.

--- task ---

### Ustaw oczy

Pierwsza liczba w ` ` to środek oka. Oczy powinny być ustawione w tej samej odległości od środka rysunku.

W tym przykładzie ` ` i ` ` to piksele ` 40` oddalone od 200, co działa dla rysunku o szerokości 400.

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Black — change to red, green, or blue up to 255
    eye_size = 50
    ellipse(160, 180, eye_size, eye_size)  # x, y, width, height
    ellipse(240, 180, eye_size, eye_size)

--- /code ---

** Wskazówka:** Jeśli chcesz mieć okrągłe oczy, użycie zmiennej ` eye_` ułatwia zmianę szerokości i wysokości obu oczu w jednym miejscu.

[[[processing-python-ellipse]]]

--- collapse ---

---
Title: Obliczanie pozycji na podstawie szerokości
---

Środek rysunku znajduje się w pozycji ` width / 2 ` lub o połowę szerokości. Możesz użyć tej opcji, aby ustawić oczy, odejmując szerokość lewego oka i dodając ją dla prawego oka:

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Black — change to red, green, or blue up to 255
    eye_size = 50
    ellipse( (width / 2) - 40, 180, eye_size, eye_size)  # x, y, width, height
    ellipse( (width / 2) + 40 , 180, eye_size, eye_size)

--- /code ---

Możesz również obliczyć szerokość oczu na podstawie szerokości rysunku.

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Black — change to red, green, or blue up to 255
    ellipse( (width / 2) - (width / 10) , 180, eye_size, eye_size)  # x, y, width, height
    ellipse( (width / 2) + (width / 10) , 180, eye_size, eye_size)

--- /kod ---

--- /collapse ---

Zmień drugą liczbę w wywołaniu funkcji ` ` , aby przesunąć pozycję ` ` (pionową) oczu.

--- /task ---

--- task ---

Test **: ** zmieniaj kształt i pozycję oczu, dopóki nie spodoba Ci się ich wygląd.

** Wskazówka:** Jeśli ustawisz obrys do rysowania twarzy i nie chcesz go dla oczu, musisz zadzwonić do ` no_stroke()` przed rysowaniem oczu.

[[[processing-stroke]]]

--- /task ---

--- task ---

### Dodaj szczegóły

Możesz użyć więcej okręgów, aby utworzyć:
+ Kolorowe tęczówki
+ Czarne źrenice
+ Białe światła
+ Albo coś innego

To oko ma kolorową tęczówkę, czarną źrenicę i białe reflektory ze zmienioną nieprzezroczystością: ![Obszar wyjściowy pokazujący oko z oświetleniem źrenicy i źrenicy.](images/catchlights.png)

\[[[generic-theory-simple-colours]]\] \[[[processing-opacity\]]]

Możesz również animować oczy, obracając je.

[[[processing-rotation]]]

--- /task ---

--- task ---

Test **: ** zmieniaj oczy, aż spodoba Ci się ich wygląd.

Czy Twój rysunek zaczyna wyglądać jak twarz?

--- /task ---

--- task ---

** Debug:** Możesz znaleźć kilka błędów w swoim projekcie, które musisz naprawić. Oto kilka typowych robaków.

--- collapse ---
---
Title: Oczy nie są wyśrodkowane
---

Możesz użyć ` height / 2 `, aby umieścić je na środku.

--- /collapse ---

--- collapse ---
---
Title: Oczy nie są ze sobą wyrównane
---

Jeśli chcesz, aby oczy były wyrównane, upewnij się, że używasz tej samej liczby dla współrzędnych obu oczu. Spróbuj użyć zmiennej, aby wartości były zawsze takie same.

--- /collapse ---

--- collapse ---

---
Title: Nie widzę źrenicy ani tęczówki
---

Najpierw trzeba narysować oko, potem tęczówkę, a na koniec źrenicę. Kolejność rysowania rzeczy jest bardzo ważna.

Grafika komputerowa składa się z warstw. W twoim oku każda elipsa jest warstwą. Obiekty na wyższych warstwach znajdują się przed obiektami na niższych warstwach. Wyobraź sobie wycinanie wszystkich kształtów z papieru. W zależności od tego, jak układasz i nakładasz ten papier, końcowy wynik może wyglądać bardzo inaczej.

--- /collapse ---

--- collapse ---

---
Title: Moje oczy nie są okrągłe
---

Trzecia i czwarta liczba w ` ` to szerokość i wysokość oczu.

** Wskazówka:** Jeśli uczynisz je takimi samymi, dostaniesz okrągłe oczy.

--- /collapse ---


--- /task ---

--- save ---
