from p5 import *

def grid():
    push_matrix()
    stroke(200)
    fill(0)
    line(0, height/2, width, height/2)
    line(width/2, 0, width/2, height)
    x_koordinaten = [0, width/2, width]
    y_koordinaten = [0, height/2, height]
  
    for x in x_koordinaten:
        for y in y_koordinaten:
            koord_zeigen(x, y)
  
    pop_matrix()

def koord_zeigen(x, y):
    if x == width:
        x_align = RIGHT
    elif x == 0:
        x_align = LEFT
    else:
        x_align = CENTER
  
    if y == height:
        y_align = BASELINE
    elif y == 0:
        y_align = TOP
    else:
        y_align = CENTER
  
    push_matrix()
    fill(100)
    text_align(x_align, y_align)
    text('(' + str(int(x)) + ', ' + str(int(y)) + ')', x, y)
    pop_matrix()
