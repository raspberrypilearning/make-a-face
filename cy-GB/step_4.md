## Ychwanegu llygaid

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Mae llygaid yn gwneud i siâp ddechrau edrych fel wyneb.
</div>
<div>
![Yr ardal allbwn yn dangos wyneb â llygaid.](images/eyes.png){:width="200px"}
</div>
</div>

--- task ---

Meddyliwch am ba fath o lygaid sydd eu hangen ar eich wyneb. Dau gylch yw'r llygaid symlaf.

Fe allech chi ychwanegu irisau a chanhwyllau llygaid o liwiau gwahanol. Fe allech chi ychwanegu aroleuadau / goleubwyntiau ysgafn mewn lliw gwahanol.

--- /task ---

Arbrofwch gydag `ellipses` yn y swyddogaeth `draw` i greu'r llygaid rydych chi eu heisiau.

--- task ---

### Lleoli'r llygaid

Y rhif cyntaf yn `ellipse` yw canol y llygad. Dylid lleoli'r llygaid yr un pellter o ganol y lluniad.

Yn yr enghraifft hon, mae `160` a `240` `40` picsel i ffwrdd o 200, sy'n gweithio i luniad â lled o 400.

--- code ---
---
language: python
filename: main.py - draw()
---
  fill(0, 0, 0) #Black — change to red, green, or blue up to 255 eye_size = 50 ellipse(160, 180, eye_size, eye_size) #x, y, width, height ellipse(240, 180, eye_size, eye_size)

--- /code ---

**Cyngor:** Os hoffech chi gael llygaid crwn, mae defnyddio newidyn `maint_llygaid` yn ei gwneud hi'n haws newid lled ac uchder y ddwy lygad mewn un lle.

[[[processing-python-ellipse]]]

--- collapse ---

---
title: Cyfrifo lleoliad ar sail lled
---

Mae canol lluniad yn y safle `width / 2` neu hanner y lled. Fe allwch chi ddefnyddio hyn i leoli'r llygaid drwy dynnu lled y llygad ar gyfer y llygad chwith a'i ychwanegu ar gyfer y llygad dde:

--- code ---
---
language: python
filename: main.py - draw()
---

  fill(0, 0, 0) #Black — change to red, green, or blue up to 255 eye_size = 50 ellipse( (width / 2) - 40, 180, eye_size, eye_size) #x, y, width, height ellipse( (width / 2) + 40 , 180, eye_size, eye_size)

--- /code ---

Fe allech chi hefyd gyfrifo lled y llygaid ar sail lled y lluniad.

--- code ---
---
language: python
filename: main.py - draw()
---

  fill(0, 0, 0) #Black — change to red, green, or blue up to 255 ellipse( (width / 2) - (width / 10) , 180, eye_size, eye_size) #x, y, width, height ellipse( (width / 2) + (width / 10) , 180, eye_size, eye_size)

--- /code ---

--- /collapse ---

Newidiwch yr ail rif yn yr alwad swyddogaeth `ellipse` i symud safle `y` (fertigol) y llygaid.

--- /task ---

--- task ---

**Profi:** Daliwch ati i newid siâp a safle'r llygaid nes eich bod yn fodlon ar sut maen nhw'n edrych.

**Cyngor:** Os ydych chi'n gosod strôc ar gyfer llunio'r wyneb ond nad ydych chi eisiau un ar gyfer y llygaid, bydd angen i chi alw `no_stroke()` cyn llunio'r llygaid.

[[[processing-stroke]]]

--- /task ---

--- task ---

### Ychwanegu manylion

Fe allwch chi ddefnyddio mwy o gylchoedd i greu:
+ Irisau lliw
+ Canwyllau llygaid du
+ Goleubwyntiau gwyn
+ Neu rywbeth arall!

Mae gan y llygad hon iris lliw, cannwyll llygad ddu a goleubwyntiau gwyn gydag afloywder wedi'i newid: ![Yr ardal allbwn yn dangos llygad gyda goleubwyntiau dros gannwyll y llygad a'r iris.](images/catchlights.png)

\[[[generic-theory-simple-colours]]\] \[[[processing-opacity\]]]

Fe allwch chi hefyd animeiddio'r llygaid drwy eu cylchdroi.

[[[processing-rotation]]]

--- /task ---

--- task ---

**Profi:** Daliwch ati i newid y llygaid nes eich bod yn fodlon ar sut maen nhw'n edrych.

Yw eich lluniad yn dechrau edrych fel wyneb?

--- /task ---

--- task ---

**Difa chwilod:** Efallai bydd angen i chi drwsio chwilod yn eich prosiect. Dyma rai chwilod cyffredin.

--- collapse ---
---
title: Dydy'r llygaid ddim wedi'u canoli
---

Fe allech chi ddefnyddio `height / 2` i'w lleoli yn y canol.

--- /collapse ---

--- collapse ---
---
title: Dydy'r llygaid ddim yn gyflin
---

Os ydych chi am i'r llygaid fod yn gyflin, gwnewch yn siŵr eich bod yn defnyddio'r un rhif ar gyfer cyfesurynnau'r ddwy lygad. Rhowch gynnig ar ddefnyddio newidyn fel bod y gwerthoedd yr un fath bob amser.

--- /collapse ---

--- collapse ---

---
title: Dydw i ddim yn gallu gweld cannwyll y llygad neu'r iris
---

Mae angen llunio'r llygad gyntaf, yna'r iris, a channwyll y llygad yn olaf. Mae'r drefn rydych chi'n llunio pethau ynddi yn bwysig iawn.

Mae graffeg cyfrifiadurol wedi'i gwneud o haenau. Yn eich llygad, mae pob elips yn haen. Mae gwrthrychau ar haenau uwch yn eistedd o flaen gwrthrychau ar haenau is. Dychmygwch dorri'r holl siapiau allan o bapur. Yn dibynnu ar sut rydych chi'n trefnu ac yn croesi'r papur hwnnw, gallai'r canlyniad edrych yn wahanol iawn.

--- /collapse ---

--- collapse ---

---
title: Dydy fy llygaid ddim yn grwn
---

Y trydydd a'r pedwerydd rhif yn `ellipse` yw lled ac uchder y llygaid.

**Cyngor:** Os byddwch chi'n eu gwneud yr un fath, byddwch chi'n cael llygaid crwn.

--- /collapse ---


--- /task ---

--- save ---
