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

Add code to the `draw()` function to draw a face or mask.

Αυτό το παράδειγμα σχεδιάζει έναν κύκλο στη μέση, αλλά εξαρτάται από εσένα ποιο σχήμα θα χρησιμοποιήσεις.

--- code ---
---
language: python filename: main.py - draw() line_numbers: true line_number_start: 11
line_highlights: 12
---

def draw():   
ellipse(width/2, height/2, 200, 200) #Κύκλος στη μέση

    # Add code to draw your face here
    ellipse(width/2, height/2, 200, 200)  # Circle in the middle
    
    grid()  # add a # to the beginning of this line to hide the grid

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
language: python filename: main.py - draw() line_numbers: true line_number_start: 11
line_highlights: 13
---

    # Add code to draw your face here
    fill(255, 255, 0)  # Bright yellow
    ellipse(width/2, height/2, 200, 200)

--- /code ---

[[[generic-theory-simple-colours]]]

--- /task ---

--- task ---

**Test:** Run your code and change the colour until you are happy with it.

--- /task ---

--- save ---
