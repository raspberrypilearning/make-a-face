## Add more details

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Does your face or mask need more details to make it more interesting? 
</div>
<div>
![Image showing a face as an example with a headband accessory.](images/frida.png){:width="200px"}
</div>
</div>

--- task ---

You can use more shapes to add more features to your face or mask.

How can you give the face more personality? 

You could add:

+ A nose
+ Eyebrows
+ Ears 
+ Cheeks 
+ Highlights / catchlights
+ Whatever you like!

Just add the extra details that make sense for your drawing.

--- /task ---

--- task ---

You can make partly transparent colours by adding a fourth number to an RGB colour to give the **opacity**.

This code draws the overlapping highlights in the Kawaii fruit example:

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

![Kawaii fruit image with highlights at different opacities: 30, 70, 150, 255. The lower value, 30, is more opaque and 255 is less opaque.](images/opacity.png)

--- /task ---

--- save ---
