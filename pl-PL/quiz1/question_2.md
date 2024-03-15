--- question ---

---
legend: Pytanie 2 z 3
---

W swoim projekcie dodałeś kod, aby narysować ścianę z wieloma funkcjami. Kolejność kodu była niezwykle ważna, aby twarz wyglądała jak Twój projekt.

Gdybyś uruchomił ten kod, jak wyglądałaby twarz?

--- code ---
---
language: python

---

def draw():

  #Face stroke(0) #Black fill(255) #White ellipse(200, 200, 200, 190) no_stroke()

  #Eyes fill(0, 255, 0) #Green ellipse(160, 180, 60, 60) ellipse(240, 180, 60, 60) fill(0) #Black ellipse(160, 180, 30, 30) ellipse(240, 180, 30, 30)

run()

--- /code ---

--- choices ---

- ( )

![Biała twarz z czarnym konturem. Istnieją dwa stałe zielone oczy z czarnymi konturami.](images/face1.png)

 --- feedback ---

 Nie do końca, spójrz na kolejność funkcji ` elipse()` i ` stroke()`.

 --- /feedback ---

- ( )

![Biała twarz z czarnym konturem. Istnieją dwa zielone oczy z czarnymi źrenicami i oba mają czarny kontur.](images/face2.png)

 --- feedback ---

 Nie do końca, spójrz na kolejność funkcji ` stroke()`.

 --- /feedback ---

- (x)

![Biała twarz z czarnym konturem. Istnieją dwa zielone oczy z czarnymi źrenicami, a oczy nie mają konturu.](images/face3.png)

 --- feedback ---

 Poprawnie, kod rysuje twarz czarnym obrysem, a następnie wyłącza obrys przed narysowaniem okręgów. Zielone kółka są rysowane najpierw z czarnymi kółkami na górze.

 --- /feedback ---

- ( )

![Biała twarz z czarnym konturem. Istnieją dwa stałe zielone oczy, które nie mają konturu.](images/face4.png)

 --- feedback ---

 Nie do końca, spójrz na kolejność funkcji ` elipse()`.

 --- /feedback ---

--- /choices ---

--- /question ---
