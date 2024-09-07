## Scegli un tema

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Hai già idea del tipo di faccia o maschera che vuoi disegnare? Usa questo passaggio per pianificare la tua arte e impostare la tela.
</div>
<div>
![Output con una faccia di vampiro.](images/vampire.png){:width="200px"}
</div>
</div>

--- task ---

Apri il [progetto iniziale](https://editor.raspberrypi.org/en/projects/make-face-starter){:target="_blank"}. L'editor di codice Raspberry Pi si aprirà in un'altra scheda del browser.

--- /task ---

--- task ---

**Scegli:** Pensa al tipo di faccia che vuoi realizzare:
+ Vuoi scegliere qualcosa della tua tradizione o proveniente dalla cultura popolare?
+ La tua opera mostrerà un essere umano, un animale, creature mitologiche o forse una macchina?
+ Potresti anche voler creare un autoritratto!
+ Potresti disegnare un'emoji da condividere con i tuoi amici

--- /task ---

--- task ---

La prima cosa da fare quando si crea arte usando la libreria `Processing` di Pytohn è aggiungere `def setup():` per definire una funzione `setup` che viene eseguita una volta all'inizio del programma.

Il progetto iniziale ha una funzione `setup` (inizializzazione) che imposta la `size` (dimensione) della tua tela alla larghezza di `400` e altezza`400` pixel.

**Scegli:** Sperimenta i numeri ed esegui il tuo codice per trovare una dimensione che ti soddisfa.

--- collapse ---

---
title: Impostazione delle dimensioni dello schermo all'avvio del programma
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

**Scegli:** Pensa ai colori che utilizzerai per il tuo viso e cambia i valori del colore del `background` (sfondo) per assegnare un colore complementare al tuo schermo.

[[[generic-theory-simple-colours]]]

--- collapse ---

---
title: Impostazione del colore di sfondo all'avvio del programma
---

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 9
line_highlights: 9
---

    background(255, 255, 255)  # Try different numbers to change the colour

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Suggerimento:** La funzione `draw` ha un comando `grid ()`. Questo aggiunge una griglia di coordinate sullo sfondo, per aiutarti a capire dove posizionare le parti del viso.

Per disattivare la griglia, aggiungi un `#` all'inizio della riga, per ripristinarla rimuovilo `#`.

--- code ---
---
language: python
filename: main.py - draw()
---

    grid()  # Shows grid

--- /code ---

--- code ---
---
language: python
filename: main.py - draw()
---

    #grid()  # Hide grid by turning it into a comment

--- /code ---

--- /task ---

--- task ---

**Test:** Esegui il tuo progetto per verificare la dimensione dello schermo e il colore dello sfondo scelti.

--- /task ---

--- task ---

**Debug:** Potresti trovare alcuni bug nel tuo progetto, dovrai correggerli. Ecco alcuni bug comuni.

--- collapse ---

---
title: Ho aggiornato le mie dimensioni e il mio colore ma l'output rimane lo stesso
---

Dopo aver modificato il codice, dovrai premera **`Run (Esegui)** per vedere le modifiche nell'area di output.

--- /collapse ---

--- collapse ---

---
title: Ho provato numeri diversi ma il colore di sfondo non cambia
---

La quantità massima di rosso, verde o blu è `255`. Assicurati che tutti i valori di colore `background` siano compresi tra `0` e`255`.

--- /collapse ---

--- /task ---

--- save ---
