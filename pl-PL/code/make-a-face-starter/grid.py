from p5 import *

def grid():
    push_matrix()
    stroke(200)
    fill(0)
    linia(0, wysokość/2, szerokość, wysokość/2)
    linia(szerokość/2, 0, szerokość/2, wysokość)
    x_coords = [0, width/2, width]
    y_współrzędne = [0, height/2, height]
  
    dla x in x_coords:
        for y in y_coords:
            pokaż_coord(x, y)
  
    pop_matrix()

def show_coord(x, y):
    if x == szerokość:
        X_align = W PRAWO
    elif x == 0:
        X_align = LEWO
    inne:
        X_align = ŚRODEK
  
    if y == wysokość:
        y_align = LINIA BAZOWA
    elif y == 0:
        y_align = GÓRA
    inne:
        y_align = ŚRODEK
  
    push_matrix()
    wypełnienie(100)
    text_align(x_align, y_align)
    text(' + str(int(x)) + ', ' + str(int(y)) + ')', x, y)
    pop_matrix()
