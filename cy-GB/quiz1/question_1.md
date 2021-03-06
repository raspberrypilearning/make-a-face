## Beth nesaf?

Da iawn! Rydych chi wedi dysgu cryn dipyn! Amser myfyrio nawr — mae myfyrio'n rhan bwysig o ddysgu oherwydd mae'n helpu i wneud cysylltiadau newydd yn eich ymennydd.

Atebwch y tri chwestiwn isod i fyfyrio ar yr hyn rydych chi wedi'i ddysgu.

Ar ôl bob cwestiwn, pwyswch **cyflwyno**. Byddwch chi'n cael eich tywys i'r ateb cywir. Fe allwch chi wneud y gweithgaredd hwn cymaint ag y mynnwch.

Mwynhewch!

--- question ---
---
legend: Cwestiwn 1 o 3
---

Yn eich prosiect, roeddech chi wedi llunio cegau gan ddefnyddio siapiau.

Pa fath o geg fyddai'r cod hwn yn ei llunio?

--- code ---
---
language: python
---

def draw(): 
  fill(0, 0, 0) #Du 
  ellipse(160, 200, 150, 150) 
  fill(255, 255, 255) #Gwyn 
  ellipse(160, 150, 150, 150)

--- /code ---

--- choices ---

- ( ) ![](images/sad-mouth.png)

  --- feedback ---

  Ddim yn hollol, i greu ceg drist byddai angen i'r ail `ellipse` gael **y_coordinate** sy'n is na'r `ellipse` cyntaf.

  --- /feedback ---

- (x) ![](images/happy-mouth.png)

  --- feedback ---

  Cywir! Mae'r ail `ellipse` yn cael ei lunio â **y_coordinate** sy'n uwch na'r `ellipse` cyntaf.

  --- /feedback ---

- () ![](images/circle-mouth.png)

  --- feedback ---

   Ddim yn hollol, mae gan yr ail gylch `fill(255, 255, 255)` gwyn ac mae wedi'i leoli'n rhannol dros y cylch du cyntaf.

  --- /feedback ---

- ( ) ![](images/square-mouth.png)

  --- feedback ---

Dydy'r cod ddim yn llunio petryalau. Mae'r swyddogaeth `ellipse` yn llunio cylchoedd.

  --- /feedback ---

--- /choices ---

--- /question ---
