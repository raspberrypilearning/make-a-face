#!/bin/python3

from p5 import *
from grid import *


def setup():
    # Metti qui sotto il codice che verrà eseguito una sola volta
    size(400, 400)  # larghezza e altezza


def draw():
    # Metti qui sotto il codice che verrà eseguito ad ogni frame
    background(255, 255, 255)
    # Aggiungi il codice per disegnare la tua faccia qui

    grid() # aggiungi un # all'inizio di questa riga per nascondere la griglia


# Non cancellare quest'ultima istruzione, serve ad eseguire il codice
run()
