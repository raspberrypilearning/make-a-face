## Aggiungi ulteriori dettagli

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Il tuo viso o la tua maschera hanno bisogno di maggiori dettagli per diventare più interessanti? 
</div>
<div>
![Immagine che mostra un volto come esempio con una fascia per capelli.](images/frida.png){:width="200px"}
</div>
</div>

--- task ---

Puoi utilizzare più forme per aggiungere più funzionalità al tuo viso o alla tua maschera.

Come dare più personalità al viso?

Potresti aggiungere:

+ Un naso
+ Sopracciglia
+ Orecchie
+ Guance
+ Riflessi/lucchichio
+ Qualunque cosa ti piaccia!

Aggiungi ulteriori dettagli che abbiano senso per il tuo disegno.

--- /task ---

--- task ---

Puoi rendere i colori parzialmente trasparenti, aggiungendo un quarto valore al colore RGB, per impostare l'**opacità**.

Questo codice disegna i riflessi sovrapposti, nell'esempio del frutto Kawaii:

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

![Immagine di frutta kawaii con riflessi a differenti valori di opacità: 30, 70, 150, 255. Il valore più basso, 30, è meno opaco mentre 255 è completamente opaco.](images/opacity.png)

--- /task ---

--- save ---
