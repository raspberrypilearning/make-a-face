#!/bin/python3

from p5 import *
from grid import *


def setup():
    # Code, der hier steht, wird einmal ausgeführt
    size(400, 400)  # Breite und Höhe


def draw():
    # Code, der hier steht, wird jeden Frame ausgeführt
    background(255, 255, 255)
    # Füge hier Code hinzu, um dein Gesicht zu zeichnen

    grid()  # füge am Anfang dieser Zeile ein # hinzu, um das Raster auszublenden


# Lass dies so stehen, um deinen Code auszuführen
run()
