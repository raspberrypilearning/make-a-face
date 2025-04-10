## Швидкий тест

Дай відповідь на три запитання. Підказки допоможуть знайти правильну відповідь.

Відповівши на кожне питання, натисни на **Перевірити мою відповідь**.

Успіхів!

--- question ---

---
legend: Питання 1 з 3
---

У своєму проєкті ти малюєш рот за допомогою фігур.

Який рот намалює цей код?

--- code ---
---
language: python

---
def draw():
  fill(0, 0, 0) # Чорний
  ellipse(160, 200, 150, 150)
  fill(255, 255, 255) # Білий
  ellipse(160, 150, 150, 150)

--- /code ---

--- choices ---

- ( ) ![](images/sad-mouth.png)

  --- feedback ---

  Не зовсім так. Щоб створити сумний рот, другому колу (`ellipse`) потрібна **координата y**, яка знаходиться нижче першого кола.

  --- /feedback ---

- (x) ![](images/happy-mouth.png)

  --- feedback ---

  Правильно! Друге коло (`ellipse`) намальовано з **координатою y**, вищою за перше коло.

  --- /feedback ---

- () ![](images/circle-mouth.png)

  --- feedback ---

   Не зовсім так. Друге коло має білий колір заливки (`fill(255, 255, 255)`) та частково знаходиться над першим чорним колом.

  --- /feedback ---

- ( ) ![](images/square-mouth.png)

  --- feedback ---

Цей код не малює прямокутники. Функція `ellipse` малює кола.

  --- /feedback ---

--- /choices ---

--- /question ---
