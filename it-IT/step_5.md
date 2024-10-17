## Aggiungi una bocca

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Una bocca è un ottimo modo per mostrare emozioni. Il tuo personaggio avrà un sorriso, un broncio o che altro? 
</div>
<div>
![Immagine che mostra una faccia da robot come esempio di faccia con una bocca.](images/mask.png){:width="200px"}
</div>
</div>

--- task ---

Pensa a quale tipo di bocca ha bisogno la tua faccia. La bocca più semplice potrebbe essere un cerchio, per esprimere sorpresa.

Potresti aggiungere due cerchi sovrapposti per creare un sorriso o un broncio. Triangoli o rettangoli potrebbero essere usati per i denti.

--- /task ---

--- task ---

Aggiungi il tuo codice alla funzione `draw()` per aggiungere una bocca.

--- collapse ---

---
title: Crea una bocca sovrapponendo dei cerchi
---

Imposta il colore di riempimento `fill` per la bocca, quindi disegna un'`ellisse`. Imposta di nuovo il colore con `fill`, questa volta scegliendo il colore della faccia, quindi disegna una seconda `ellisse`.

Cambia la coordinata `y` della seconda `ellisse` in una posizione leggermente superiore per un sorriso o in una posizione leggermente inferiore per un broncio.

![L'output che mostra una bocca sorridente.](images/smile.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Una bocca nera
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0)  # Una faccia arancione
    ellipse(200, 235, 15, 15)  # Cerchio superiore

--- /code ---

![L'output che mostra una faccia imbronciata.](images/frown.png)

--- code ---
---
language: python
filename: main.py - draw()
---

    fill(0, 0, 0)  # Una bocca nera
    ellipse(200, 240, 15, 15)
    fill(255, 165, 0)  # Una faccia arancione
    ellipse(200, 245, 15, 15)  # Cerchio inferiore

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Crea una bocca usando dei rettangoli
---

Spesso i robot sono rappresentati con bocche a forma di `rettangolo`. A volte `rettangoli` ed `ellissi` vengono usati insieme per creare un'emoji che fa una boccaccia o per aggiungere una mascherina.

![L'output che mostra una faccia con una mascherina.](images/rectangle-mask.png)

Aggiungi il codice per un `rettangolo`, quindi crea un `rettangolo` più piccolo al suo interno. Cambia i colori con `stroke` e `fill` per completare il tuo tema. Aggiungi delle `ellissi` se necessario.

**Suggerimento:** Ricorda di mettere le `ellissi` prima del codice del `rettangolo` se vuoi che vadano dietro al `rettangolo`.

--- code ---
---
language: python
filename: main.py - draw()
---

    # Mascherina
    no_fill()
    stroke(255, 255, 255)
    ellipse(150, 250, 30, 30)  # Cerchio per l'orecchio sinistro
    ellipse(250, 250, 30, 30)  # Cerchio per l'orecchio destro
    fill(255, 255, 255)
    no_stroke()
    rect(150, 230, 100, 40)  # Grande rettangolo bianco
    fill(108, 200, 206)
    rect(152, 235, 96, 30)  # Rettangolo blu più piccolo

--- /code ---

--- /collapse ---

**Suggerimento:** Aggiungi il commento `# Bocca` sulla riga prima del codice della bocca per aiutarti a trovare facilmente il codice che crea la bocca.

--- /task ---

--- task ---

**Scegli:** Potresti anche aggiungere più denti alla bocca, usando `translate` per modificare la coordinata `x` dopo che ogni dente è stato disegnato.

--- collapse ---

---
title: Usa un ciclo per aggiungere una fila di denti
---

Aggiungi il codice per creare un ciclo `for` che si ripete per creare il numero di denti di cui hai bisogno.

![L'output che mostra una faccia di robot con una fila di denti rettangolare di colori diversi.](images/robot-teeth.png)

Dopo che ogni dente è stato disegnato, aggiungi la funzione `translate()` per spostarti in base larghezza del dente.

Puoi anche aggiungere codice per modificare il colore di ciascun dente.

--- code ---
---
language: python
filename: main.py - draw()
---

    # Bocca
    fill(90, 110, 184)
    red = 90  # Quantità iniziale di rosso
    green = 110  # Quantità iniziale di verde
    blue = 180  # Quantità iniziale di blu
    for i in range (0,6):
        rect(100, 300, 33, 50)
        fill(red, green, blue)  # Utilizza le variabili per controllare il cambiamento di colore in ogni ciclo
        red = red+40
        blue = blue-30
        translate(33, 0)  # Muoviti lungo la coordinata x della larghezza di un dente


--- /code ---

--- /collapse ---

[[[processing-translation]]]

--- collapse ---

---
title: Usa dei triangoli per aggiungere delle zanne
---

Crea un `rettangolo` da usare come linea della bocca.

Aggiungi due `triangoli` per creare le zanne. Cambia le coordinate `x` di ogni vertice per posizionare le zanne alle estremità della bocca.

![L'output che mostra una faccia da vampiro con una bocca rettangolare e due denti triangolari.](images/vampire.png)

--- code ---
---
language: python
filename: main.py - draw()
---
    # Mouth
    fill(0)
    rect(170, 260, 60, 5)  # Linea della bocca
    fill(0)
    triangle(170, 260, 180, 280, 190, 260)  # Dente sinistro
    triangle(210, 260, 220, 280, 230, 260)  # Dente destro
--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Debug:** Potresti trovare alcuni bug da correggere nel tuo progetto. Ecco alcuni bug tra i più comuni.

--- collapse ---

---
title: La forma sovrapposta esce dal viso
---

Se usi due forme sovrapposte per creare una bocca, è necessario assicurarsi che la forma, che ha lo stesso colore della faccia, non esca dalla faccia. Se succede, cambia la larghezza o l'altezza della forma in modo che sia abbastanza piccola da stare all'interno del viso.

--- /collapse ---


--- collapse ---

---
title: Ho troppi denti
---

Non dimenticare che `range()` crea una sequenza di numeri a partire da 0 e non da 1. Questo può causare problemi al tuo codice, a seconda di come hai posizionato i denti.

--- /collapse ---

--- /task ---

--- save ---
