#!/bin/python3

from p5 import *


def setup():
    size(400, 600)
    background(255, 255, 255)
    no_stroke()


def draw():
    blau = Color(92, 204, 206)
    gruen = Color(149, 212, 122)
    rot = Color(239, 62, 91)
    lila = Color(75, 37, 109)
    braun = Color(178, 162, 150)
    grau = Color(201, 201, 201)
    flieder = Color(160, 158, 214)

    # Oberes Gesicht, Hintergrund
    fill(blau)
    rect(50, 100, 300, 200)
    fill(0)

    # Oberes Gesicht, Haare
    fill(lila)
    abstand = 0
    for i in range(0, 5):
        triangle(100+abstand, 140, 120+abstand, 120, 140+abstand, 140)
        abstand = abstand+40

    # Oberes Gesicht, linkes Auge
    fill(grau)
    rect(80, 190, 100, 50)
    fill(rot)
    triangle(190, 250, 70, 150, 180, 160)
    fill(gruen)
    triangle(190, 250, 60, 160, 180, 170)
    fill(flieder)
    ellipse(160, 200, 30, 30)

    # Oberes Gesicht, rechtes Auge
    fill(grau)
    rect(220, 190, 100, 50)
    fill(rot)
    triangle(210, 250, 330, 150, 220, 160)
    fill(gruen)
    triangle(210, 250, 340, 160, 220, 170)
    fill(flieder)
    ellipse(240, 200, 30, 30)

    # Oberes Gesicht, Mund
    fill(braun)
    rect(100, 220, 200, 50)
    fill(lila)
    rect(110, 240, 180, 10)

  # Unteres Gesicht, Hintergrund
    fill(lila)
    rect(50, 300, 300, 200)
    fill(0)

    # Unteres Gesicht, Haare
    fill(gruen)
    abstand = 0
    for i in range(0, 5):
        triangle(100+abstand, 340, 120+abstand, 320, 140+abstand, 340)
        abstand = abstand+40

    # Unteres Gesicht, linkes Auge
    fill(rot)
    rect(80, 390, 100, 50)
    fill(flieder)
    triangle(190, 450, 70, 350, 180, 360)
    fill(braun)
    triangle(190, 450, 60, 360, 180, 370)
    fill(lila)
    ellipse(160, 400, 30, 30)

    # Unteres Gesicht, rechtes Auge
    fill(rot)
    rect(220, 390, 100, 50)
    fill(flieder)
    triangle(210, 450, 330, 350, 220, 360)
    fill(braun)
    triangle(210, 450, 340, 360, 220, 370)
    fill(lila)
    ellipse(240, 400, 30, 30)

    # Unteres Gesicht, Mund
    fill(gruen)
    rect(100, 420, 200, 50)
    fill(rot)
    rect(110, 440, 180, 10)


run()
