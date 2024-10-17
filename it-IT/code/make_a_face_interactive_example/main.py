#!/bin/python3

from p5 import *
from random import randint


def sad(x_middle, y_eye, y_mouth):
    ellipse(x_middle - 50, y_eye - 20, 60, 50)  # x, y, larghezza, altezza
    ellipse(x_middle + 50, y_eye - 20, 60, 50)
    ellipse(x_middle, y_mouth + 30, 100, 65)


def happy(x_middle, y_eye, y_mouth):
    ellipse(x_middle - 50, y_eye + 20, 60, 50)  # x, y, larghezza, altezza
    ellipse(x_middle + 50, y_eye + 20, 60, 50)
    ellipse(x_middle, y_mouth - 30, 100, 65)


def setup():
    # Metti qui il codice che verrà eseguito una sola volta
    size(400, 400)  # larghezza e altezza
    background(0, 0, 0) # sposta questo comando sotto draw() se vuoi ripristinare il disegno a ogni frame
    rect_mode(CENTER)
    no_stroke()


def draw():
    # Metti qui sotto il codice che verrà eseguito ogni per ogni frame
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
    # copre parzialmente occhi e bocca
    fill(255)
    if mouse_x > x_middle:
        happy(x_middle, y_eye, y_mouth)
    else:
        sad(x_middle, y_eye, y_mouth)
    # copre la parte superiore della maschera
    fill(0)
    ellipse(x_middle, 60, 250, 90)
    # ombreggia metà della maschera
    fill(0, 25)
    rect(300, 200, width/2, height)


def mouse_pressed():
    # Inserisci qui il codice da eseguire quando viene premuto il mouse
    print(mouse_x, mouse_y)


# Non cancellare quest'ultima istruzione, serve a eseguire il codice
run()
