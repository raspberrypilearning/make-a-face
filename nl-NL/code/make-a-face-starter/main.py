#!/bin/python3

from p5 import *
from grid import *


def setup():
    # Zet de code om eenmalig uit te voeren hier onder
    size(400, 400) # breedte en hoogte


def draw():
    # Zet hier code om bij elk frame uit te voeren
    background(255, 255, 255)
    # Voeg hier code toe om je gezicht te tekenen

    grid()  # add a # to the beginning of this line to hide the grid


# Keep this to run your code
run()
