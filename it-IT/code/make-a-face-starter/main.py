#!/bin/python3

from p5 import *
from grid import *


def setup():
    # Metti qui sotto il codice che verrà eseguito una sola volta
    size(400, 400)  # larghezza e altezza


def draw():
    # Metti qui sotto il codice che verrà eseguito ad ogni cambio di frame
    background(255, 255, 255)
    # Add code to draw your face here

    grid()  # add a # to the beginning of this line to hide the grid


# Keep this to run your code
run()
