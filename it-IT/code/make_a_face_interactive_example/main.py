#!/bin/python3

from p5 import *
from random import randint


def sad(x_middle, y_eye, y_mouth):
    ellipse(x_middle - 50, y_eye - 20, 60, 50)  # x, y, width, height
    ellipse(x_middle + 50, y_eye - 20, 60, 50)
    ellipse(x_middle, y_mouth + 30, 100, 65)


def happy(x_middle, y_eye, y_mouth):
    ellipse(x_middle - 50, y_eye + 20, 60, 50)  # x, y, width, height
    ellipse(x_middle + 50, y_eye + 20, 60, 50)
    ellipse(x_middle, y_mouth - 30, 100, 65)


def setup():
    # Metti qui sotto il codice che verrà eseguito una sola volta
    size(400, 400)  # larghezza e altezza
    background(0, 0, 0) # spostati sotto draw() per ripristinare il disegno ad ogni fotogramma
    rect_mode(CENTER)
    no_stroke()


def draw():
    # Metti qui sotto il codice che verrà eseguito ad ogni cambio di frame
    mask_width = width / 2
    x_middle = width / 2
    y_eye = 180
    y_mouth = 255
    # disegna la maschera
    fill(255, 255, 255)  # bianco
    rect(200, 150, mask_width, mask_width)
    ellipse(x_middle, 250, mask_width, 140)
    # occhi e bocca
    fill(0)  # nero
    ellipse(x_middle - 50, y_eye, 60, 50)  # x, y, larghezza, altezza
    ellipse(x_middle + 50, y_eye, 60, 50)
    ellipse(x_middle, y_mouth, 100, 75)
    # coprire parzialmente occhi e bocca
    fill(255)
    if mouse_x > x_middle:
        happy(x_middle, y_eye, y_mouth)
    else:
        sad(x_middle, y_eye, y_mouth)
    # coprire la parte superiore della maschera
    fill(0)
    ellipse(x_middle, 60, 250, 90)
    # ombreggiare metà della maschera
    fill(0, 25)
    rect(300, 200, width/2, height)


def mouse_pressed():
    # Inserisci qui il codice da eseguire quando si preme il mouse
    print(mouse_x, mouse_y)


# Conserva questa parte per eseguire il codice
run()
