## Dodaj więcej szczegółów

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Czy Twoja twarz lub maska potrzebują więcej szczegółów, aby uczynić ją bardziej interesującą? 
</div>
<div>
![Obraz przedstawiający twarz jako przykład z dodatkiem pałąka na głowę.](images/frida.png){:width="200px"}
</div>
</div>

--- task ---

Możesz użyć więcej kształtów, aby dodać więcej operacji do swojej twarzy lub maski.

Jak możesz nadać twarzy więcej osobowości?

Możesz dodać:

+ Nos
+ Brwi
+ Uszy
+ Policzki
+ Podświetlenie / podświetlenie
+ Co chcesz!

Wystarczy dodać dodatkowe szczegóły, które mają sens dla twojego rysunku.

--- /task ---

--- task ---

Możesz stworzyć częściowo przezroczyste kolory, dodając czwartą liczbę do koloru RGB, aby nadać przezroczystość ** **.

Ten kod rysuje nakładające się podświetlenia w przykładzie owocu Kawaii:

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

![Obraz owocu Kawaii z podświetleniami o różnych nieprzezroczystościach: 30, 70, 150, 255. Niższa wartość, 30, jest bardziej nieprzezroczysta, a 255 mniej nieprzezroczysta.](images/opacity.png)

--- /task ---

--- save ---
