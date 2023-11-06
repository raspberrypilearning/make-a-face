## Dewis thema

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Oes gennych chi sniad pa fath o wyneb neu fasg hoffech chi ei wneud? Defnyddiwch y cam hwn i gynllunio eich celf a gosod eich canfas.
</div>
<div>
![Yr ardal allbwn gydag wyneb ar thema fampir.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Open the [starter project](https://editor.raspberrypi.org/en/projects/make-face-starter){:target="_blank"}. The Raspberry Pi code editor will open in another browser tab.

--- /task ---

--- task ---

**Dewis:** Meddyliwch am ba fath o wyneb hoffech chi ei wneud:
+ Ydych chi am ddewis rhywbeth o'ch treftadaeth neu ddiwylliant poblogaidd?
+ Fydd eich celf yn dangos person, anifail, rhywbeth chwedlonol, neu beiriant efallai?
+ Fe allech chi wneud hunanbortread hyd yn oed!
+ Fe allech chi lunio emoji i'w rannu â'ch ffrindiau

--- /task ---

--- task ---

Y peth cyntaf i'w wneud wrth greu celf gan ddefnyddio `Llyfrgell brosesu` Python yw ychwanegu `def setup():` i ddiffinio swyddogaeth `setup` sy'n rhedeg unwaith ar ddechrau eich rhaglen.

Mae gan y prosiect dechreuol swyddogaeth `setup` sy'n gosod maint eich canfas i `400` o led a `400` o uchder.

**Dewis:** Arbrofwch gyda'r rhifau a rhedeg eich cod i ganfod maint rydych chi'n fodlon arno.

--- collapse ---

---
title: Gosod maint y sgrin pan fydd eich rhaglen yn dechrau
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

**Dewis:** Meddyliwch am y lliwiau byddwch chi'n eu defnyddio ar gyfer eich wyneba newid y gwerthoedd lliw `background` i osod eich sgrin ar liw cyflenwol.

[[[generic-theory-simple-colours]]]

--- collapse ---

---
title: Gosod y lliw cefndir pan fydd eich rhaglen yn dechrau
---

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 9
line_highlights: 9
---

    background(255, 255, 255) #Rhowch gynnig ar wahanol rifau i newid y lliw

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Cyngor:** Mae gan y swyddogaeth `draw` god `grid()`. Mae hwn yn ychwanegu grid cyfesurynnau dros eich cefndir sy'n eich helpu i wybod ble i leoli nodweddion ar eich wyneb.

I gael gwared ar y grid, ychwanegwch `#` o flaen y cod, ac i'w ychwanegu eto tynnwch y `#`.

--- code ---
---
language: python
filename: main.py - draw()
---

    grid() #Dangos grid

--- /code ---

--- code ---
---
language: python
filename: main.py - draw()
---

    #grid() #Cuddio grid drwy ei droi'n sylw

--- /code ---

--- /task ---

--- task ---

**Profi:** Rhedwch eich prosiect i weld maint y sgrin a'r lliw cefndir o'ch dewis.

--- /task ---

--- task ---

**Difa chwilod:** Efallai bydd angen i chi drwsio chwilod yn eich prosiect. Dyma rai chwilod cyffredin.

--- collapse ---

---
title: Dwi wedi diweddaru fy maint a fy lliw ond mae'r ardal allbwn yn dal yr un fath
---

Ar ôl newid y cod, bydd angen i chi redeg eich prosiect gyda `run` i weld y newidiadau yn yr ardal allbwn.

--- /collapse ---

--- collapse ---

---
title: Dwi wedi rhoi cynnig ar wahanol rifau ond dydy'r lliw cefndir ddim yn newid
---

Y lefel uchaf o goch, gwyrdd neu las yw `255`. Gwnewch yn siŵr bod eich holl werthoedd lliw `background` rhwng `0` a `255`.

--- /collapse ---

--- /task ---

--- save ---
