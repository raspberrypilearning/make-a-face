--- question ---
---
legend: Cwestiwn 2 o 3
---

Yn eich prosiect, roeddech chi wedi ychwanegu cod i lunio wyneb â nifer o nodweddion. Roedd trefn eich cod yn bwysig iawn i wneud yn siŵr bod y wyneb yn edrych fel eich dyluniad.

Pe baech chi'n rhedeg y cod hwn, sut fyddai'r wyneb yn edrych?

--- code ---
---
language: python
---

def draw():

  #Wyneb
  stroke(0) #Du
  fill(255) #Gwyn
  ellipse(200, 200, 200, 190)
  no_stroke()
  
  #Llygaid
  fill(0, 255, 0) #Gwyrdd
  ellipse(160, 180, 60, 60)
  ellipse(240, 180, 60, 60)
  fill(0) #Du
  ellipse(160, 180, 30, 30)
  ellipse(240, 180, 30, 30)
  
run()

--- /code ---

--- choices ---

- ( )

![Wyneb gwyn ag amlinell ddu. Mae dwy lygad werdd soled ag amlinellau du.](images/face1.png)

 --- feedback ---

 Ddim yn hollol, 'drychwch ar drefn y swyddogaethau `ellipse()` a `stroke()`.

 --- /feedback ---

- ( )

![Wyneb gwyn ag amlinell ddu. Mae dwy lygad werdd â channwyll llygad ddu ac mae gan y ddwy amlinell ddu.](images/face2.png)

 --- feedback ---

 Ddim yn hollol, 'drychwch ar drefn y swyddogaethau `stroke()`.

 --- /feedback ---

- (x)

![Wyneb gwyn ag amlinell ddu. Mae dwy lygad werdd â channwyll llygad ddu a does gan y llygaid ddim amlinell.](images/face3.png)

 --- feedback ---

 Cywir, mae'r cod yn llunio wyneb â strôc ddu ac yna'n diffodd y strôc cyn llunio'r cylchoedd. Mae'r cylchoedd gwyrdd yn cael eu llunio gyntaf, â'r cylchoedd du ar eu pen.

 --- /feedback ---

- ( )

![Wyneb gwyn ag amlinell ddu. Mae dwy lygad werdd soled heb amlinellau.](images/face4.png)

 --- feedback ---

 Ddim yn hollol, 'drychwch ar drefn y swyddogaethau `ellipse()`.

 --- /feedback ---

--- /choices ---

--- /question ---
