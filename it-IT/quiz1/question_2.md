--- question ---

---
legend: Domanda 2 di 3
---

Nel tuo progetto hai aggiunto il codice per disegnare un volto con molte funzionalità. L'ordine con cui hai scritto il codice era fondamentale per far sì che il volto assomigliasse al tuo disegno.

Se eseguissi questo codice, come apparirebbe la faccia?

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

![Una faccia bianca con contorno nero. Ci sono due occhi verdi con contorni neri.](images/face1.png)

 --- feedback ---

 Non proprio, guarda l'ordine delle funzioni `ellipse()` e `stroke()` .

 --- /feedback ---

- ( )

![Una faccia bianca con contorno nero. Ci sono due occhi verdi con pupille nere ed entrambi hanno un contorno nero.](images/face2.png)

 --- feedback ---

 Non proprio, guarda l'ordine delle funzioni `stroke()` .

 --- /feedback ---

- (x)

![Una faccia bianca con contorno nero. Ci sono due occhi verdi con pupille nere e gli occhi non hanno un contorno.](images/face3.png)

 --- feedback ---

 Corretto, il codice disegna una faccia con un tratto nero, successivamente disattiva il tratto prima di disegnare i cerchi. I cerchi verdi vengono disegnati per primi con sopra i cerchi neri.

 --- /feedback ---

- ( )

![Una faccia bianca con contorno nero. Ci sono due occhi verdi senza contorno.](images/face4.png)

 --- feedback ---

 Non proprio, guarda l'ordine delle funzioni `ellipse()`.

 --- /feedback ---

--- /choices ---

--- /question ---
