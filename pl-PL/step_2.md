## Wybierz motyw

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Czy masz pomysł na rodzaj twarzy lub maski, którą chcesz zrobić? Użyj tego kroku, aby zaplanować swoją sztukę i skonfigurować swoje płótno.
</div>
<div>
![Obszar wyjściowy z twarzą o tematyce wampira.](images/vampir.png){:width="200px"}
</div>
</div>

--- task ---

Otwórz projekt startowy [ ](https://editor.raspberrypi.org/en/projects/make-face-starter){:target="_blank"}. Edytor kodu Raspberry Pi otworzy się w innej karcie przeglądarki.

--- /task ---

--- task ---

** Wybierz:** pomyśl o rodzaju twarzy, którą chcesz zrobić:
+ Czy chcesz wybrać coś ze swojego dziedzictwa lub kultury popularnej?
+ Czy Twoja sztuka pokaże człowieka, zwierzę, coś mitycznego, a może maszynę?
+ Możesz nawet chcieć stworzyć autoportret!
+ Możesz narysować emoji, aby udostępnić go znajomym

--- /task ---

--- task ---

Pierwszą rzeczą do zrobienia podczas tworzenia sztuki przy użyciu biblioteki przetwarzania Pythona `.` jest dodanie ` DEF setup():`, aby zdefiniować funkcję ` `, która jest uruchamiana raz na początku programu.

Projekt startowy ma funkcję ` <code> `, która ustawia rozmiar ` Twojego płótna na szerokość <code> 400 ` i wysokość </code> </code>.

** Wybierz:** eksperymentuj z liczbami i uruchom swój kod, aby znaleźć rozmiar, z którego jesteś zadowolony.

--- collapse ---

---
Title: Ustawianie rozmiaru ekranu po uruchomieniu programu
---

--- code ---
---
language: python filename: main.py - setup() line_numbers: true line_number_start: 6
line_highlights: 7
---
def setup():   
size(400, 400)  # 400 by 400 works well for a round face

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

** Wybierz:** pomyśl o kolorach użytych do twarzy i zmień wartości koloru tła ` `, aby ustawić ekran na kolor uzupełniający.

[[[generic-theory-simple-colours]]]

--- collapse ---

---
Title: Ustawianie koloru tła po uruchomieniu programu
---

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 9
line_highlights: 9
---

    background(255, 255, 255)  # Try different numbers to change the colour

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

** Wskazówka:** Funkcja ` ` ma kod ` grid()`. To dodaje siatkę współrzędnych nad tłem, która pomaga ustalić, gdzie umieścić operacje na twarzy.

Aby wyłączyć siatkę, dodaj `#` przed kodem, aby go włączyć, usuń `#`.

--- code ---
---
language: python
filename: main.py - draw()
---

    grid()  # Shows grid

--- /code ---

--- code ---
---
language: python
filename: main.py - draw()
---

    #grid()  # Hide grid by turning it into a comment

--- /code ---

--- /task ---

--- task ---

** Test:** Uruchom swój projekt, aby zobaczyć wybrany rozmiar ekranu i kolor tła.

--- /task ---

--- task ---

**Debugowanie:** Być może znajdziesz błędy w swoim projekcie, które musisz naprawić. Oto kilka typowych błędów.

--- collapse ---

---
Title: Zaktualizowałem swój rozmiar i kolor, ale obszar wyjściowy pozostaje taki sam
---

Po zmianie kodu, będziesz musiał uruchomić ** ` ` ** swój projekt, aby zobaczyć zmiany w obszarze wyjściowym.

--- /collapse ---

--- collapse ---

---
Title: Próbowałem różnych liczb, ale kolor tła się nie zmienia
---

Maksymalna ilość czerwonego, zielonego lub niebieskiego to ` 255 `. Upewnij się, że wszystkie wartości kolorów ` ` mieszczą się w przedziale ` 0 ` i ` 255 `.

--- /collapse ---

--- /task ---

--- save ---
