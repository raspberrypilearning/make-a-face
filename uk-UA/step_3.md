## Кола й еліпси

Намалюй та пофарбуй фігуру для обличчя або маски.

Функція **ellipse** створює овальну фігуру (еліпс). Якщо ти вкажеш однакову ширину й висоту, отримаєш коло.

--- task ---

Додай код до функції `draw()`, щоб установити колір заливки за допомогою значень червоного, зеленого та синього, як під час створення тла.

Потім намалюй коло цим кольором.

--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 16-22
---

def draw():
    # Тут розмісти код, який запускається на кожному кадрі
    background(255, 255, 255)  
    # Тут додай код, який малюватиме обличчя
    fill(255, 255, 0) 
    ellipse(
        screen_size/2, 
        screen_size/2, 
        200, 
        200
    )  
  
--- /code ---

--- /task ---

--- task ---

**Протестуй:** запусти код. Ти маєш побачити зафарбоване коло.

--- /task ---

--- task ---

Зміни значення ширини та висоти, і форма еліпса теж зміниться.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 18-19
---

def draw():
    # Тут розмісти код, який запускається на кожному кадрі
    background(255, 255, 255)  
    # Тут додай код, який малюватиме обличчя
    fill(255, 255, 0) 
    ellipse(
        screen_size/2, 
        screen_size/2, 
        100, # ширина
        50   # висота
    )  
  
--- /code ---

![Жовтий еліпс, ширина якого більше за висоту.](images/change_shape.png)

--- /task ---

--- task ---

Перед кодом, який малює еліпс, можна вибрати колір і товщину лінії.


--- code ---
---
language: python
line_numbers: true
line_number_start: 14
line_highlights: 15-16
---
    fill(255, 255, 0) 
    stroke(255, 255, 255)  
    stroke_weight(3)
    ellipse(
        screen_size/2, 
        screen_size/2, 
        100, 
        50
    )  
    
--- /code ---

Якщо хочеш, можеш видалити контур (функція `no_stroke`).

--- code ---
---
language: python
line_numbers: true
line_number_start: 14
line_highlights: 15
---
    fill(255, 255, 0) 
    no_stroke()
    ellipse(
        screen_size/2, 
        screen_size/2, 
        100, 
        50
    )  
  
--- /code ---

--- /task ---

--- task ---

**Протестуй:** поекспериментуй зі зміною кольору й товщиною лінії (або взагалі видали контур), а потім запусти свій код і подивись, що вийшло.

--- /task ---