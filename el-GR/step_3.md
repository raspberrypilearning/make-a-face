## Σχήμα προσώπου

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Σχεδίασε και ζωγράφισε ένα σχήμα για την φάτσα ή την μάσκα σου. Μην προσθέσεις ακόμα τις άλλες δυνατότητες, θα μπουν αργότερα.
</div>
<div>
![Εικόνα ρομπότ με τετράγωνο πρόσωπο.](images/robot-teeth.png){:width="200px"}
</div>
</div>

--- task ---

Αποφάσισε για το κύριο σχήμα του προσώπου για την μάσκα σου. Θα μπορούσε να είναι ένας κύκλος, μια έλλειψη, ένα ορθογώνιο ή ακόμα και ένα τρίγωνο.

Πρόσθεσε κώδικα στην συνάρτηση `draw()` για να σχεδιάσεις ένα πρόσωπο ή μία μάσκα. Βεβαιώσου ότι έχεις αφαιρέσει επίσης το `pass` από το εσωτερικό της συνάρτησης.

Αυτό το παράδειγμα σχεδιάζει έναν κύκλο στη μέση, αλλά εξαρτάται από εσένα ποιο σχήμα θα χρησιμοποιήσεις.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 11
line_highlights: 12
---

def draw():   
  ellipse(width/2, height/2, 200, 200) #Κύκλος στη μέση

--- /code ---

![Η περιοχή εξόδου δείχνει έναν μαύρο κύκλο στη μέση του πλέγματος.](images/black-circle.png)

[[[processing-python-ellipse]]]


[[[processing-python-rect]]]


[[[processing-python-triangle]]]

--- /task ---

--- task ---

**Δοκιμή:** Εκτέλεσε τον κώδικα σου και άλλαξε τον για να αποκτήσεις το μέγεθος και το σχήμα προσώπου που θέλεις.

--- /task ---

--- task ---

Επίλεξε ένα χρώμα περιγράμματος για το περίγραμμα και ένα χρώμα γεμίσματος για το κύριο μέρος του σχήματος.

[[[processing-stroke]]]

Εάν δεν θες ένα περίγραμμα, χρησιμοποίησε το `no_stroke()`.

--- code ---
---
language: python
filename: main.py - draw()
line_numbers: true
line_number_start: 11
line_highlights: 13
---

def draw():
  stroke(0) #Μπορείς επίσης να χρησιμοποιήσεις το no_stroke() 
  fill(255, 255, 0) #Φωτεινό κίτρινο
  ellipse(width/2, height/2, 200, 200) #Κύκλος στη μέση

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Δοκιμή:** Εκτέλεσε τον κώδικα σου και άλλαξε το χρώμα μέχρι να είσαι ευχαριστημένος/η με αυτό.

--- /task ---

--- save ---
