## Voeg meer details toe

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Heeft je gezicht of masker meer details nodig om het interessanter te maken? 
</div>
<div>
![Voorbeeld afbeelding van een gezicht met een hoofdband.](images/frida.png){:width="200px"}
</div>
</div>

--- task ---

Je kunt meer vormen gebruiken om meer elementen aan je gezicht of masker toe te voegen.

Hoe kun je het gezicht meer persoonlijkheid geven?

Je zou het volgende kunnen toevoegen:

+ Een neus
+ Wenkbrauwen
+ Oren
+ Wangen
+ Highlights/catchlights
+ Wat je maar wilt!

Voeg gewoon de extra details toe die voor je tekening zinvol zijn.

--- /task ---

--- task ---

Je kunt gedeeltelijk transparante kleuren maken door een vierde getal toe te voegen aan een RGB-kleur om de **doorzichtigheid** te geven.

Deze code tekent de overlappende highlights in het Kawaii fruit voorbeeld:

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

![Kawaii fruit afbeelding met highlights bij verschillende doorzichtigheden: 30, 70, 150, 255. De lagere waarde, 30, is minder doorzichtig en 255 is volledig doorzichtig.](images/opacity.png)

--- /task ---

--- save ---
