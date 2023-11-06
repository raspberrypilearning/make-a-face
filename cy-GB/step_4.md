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

    fill(0, 0, 0)  # Black — change to red, green, or blue up to 255
    eye_size = 50
    ellipse(160, 180, eye_size, eye_size)  # x, y, width, height
    ellipse(240, 180, eye_size, eye_size)

--- /code ---

**Tip:** If you want round eyes, then using an `eye_size` variable makes it easier to change the width and height of both eyes in one place.

[[[processing-python-ellipse]]]

--- collapse ---

---
title: Cyfrifo lleoliad ar sail lled
---

The centre of a drawing is at position `width / 2` or half the width. You can use this to position the eyes by subtracting the eye width for the left eye and adding it for the right eye:

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

fill(0, 0, 0) #Du — newid i goch, gwyrdd neu las hyd at 255 maint_llygaid = 50 ellipse( (width / 2) - 40, 180, maint_llygaid, maint_llygaid) #x, y, lled, uchder ellipse( (width / 2) + 40 , 180, maint_llygaid, maint_llygaid)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Black — change to red, green, or blue up to 255
    ellipse( (width / 2) - (width / 10) , 180, eye_size, eye_size)  # x, y, width, height
    ellipse( (width / 2) + (width / 10) , 180, eye_size, eye_size)

--- /code ---

--- /collapse ---

fill(0, 0, 0) #Du — newid i goch, gwyrdd neu las hyd at 255 ellipse( (width / 2) - (width / 10) , 180, maint_llygaid, maint_llygaid) #x, y, lled, uchder ellipse( (width / 2) + (width / 10) , 180, maint_llygaid, maint_llygaid)

--- /task ---

--- task ---

Newidiwch yr ail rif yn yr alwad swyddogaeth `ellipse` i symud safle `y` (fertigol) y llygaid.

**Tip:** If you set a stroke for drawing the face and don't want one for the eyes, then you will need to call `no_stroke()` before drawing the eyes.

[[[processing-stroke]]]

--- /task ---

--- task ---

### Ychwanegu manylion

You can use more circles to create:
+ Irisau lliw
+ Canwyllau llygaid du
+ Goleubwyntiau gwyn
+ Neu rywbeth arall!

This eye has a coloured iris, black pupil, and white catchlights with changed opacity: ![The output area showing an eye with catchlights over the pupil and iris.](images/catchlights.png)

\[[[generic-theory-simple-colours]]\] \[[[processing-opacity\]]]

Fe allwch chi ddefnyddio mwy o gylchoedd i greu:

[[[processing-rotation]]]

--- /task ---

--- task ---

**Test:** Keep changing the eyes until you like the way they look.

Is your drawing starting to look like a face?

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---
---
title: Dydy'r llygaid ddim wedi'u canoli
---

You could use `height / 2` to place them in the centre.

--- /collapse ---

--- collapse ---
---
title: Dydy'r llygaid ddim yn gyflin
---

If you want the eyes to be aligned, then make sure you use the same number for the coordinates for both eyes. Try using a variable so that the values are always the same.

--- /collapse ---

--- collapse ---

---
title: Dydw i ddim yn gallu gweld cannwyll y llygad neu'r iris
---

The eye needs to be drawn first, then the iris, and finally the pupil. The order in which you draw things is very important.

Computer graphics are made of layers. In your eye, each ellipse is a layer. Objects on higher layers sit in front of objects on lower layers. Imagine cutting all the shapes out of paper. Depending on how you arrange and overlap that paper, the final result could look very different.

--- /collapse ---

--- collapse ---

---
title: Dydy fy llygaid ddim yn grwn
---

Mae graffeg cyfrifiadurol wedi'i gwneud o haenau. Yn eich llygad, mae pob elips yn haen. Mae gwrthrychau ar haenau uwch yn eistedd o flaen gwrthrychau ar haenau is. Dychmygwch dorri'r holl siapiau allan o bapur. Yn dibynnu ar sut rydych chi'n trefnu ac yn croesi'r papur hwnnw, gallai'r canlyniad edrych yn wahanol iawn.

**Tip:** If you make them the same, you will get round eyes.

--- /collapse ---


--- /task ---

--- save ---
