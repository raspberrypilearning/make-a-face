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

    # Hintergrund des oberen Gesichts
    fill(blau)
    rect(50, 100, 300, 200)
    fill(0)

    # Haare im oberen Gesicht
    fill(flieder)
    luecke = 0
    for i in range(0, 5):
        triangle(100+luecke, 140, 120+luecke, 120, 140+luecke, 140)
        luecke = luecke+40

    # Oberes Gesicht, linkes Auge
    fill(gruen)
    rect(80, 190, 100, 50)
    fill(rot)
    triangle(190, 250, 70, 150, 180, 160)
    fill(gruen)
    triangle(190, 250, 60, 160, 180, 170)
    fill(flieder)
    ellipse(160, 200, 30, 30)

    # Oberes Gesicht, rechtes Auge
    fill(gruen)
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

  # Hintergrund des unteren Gesichts
    fill(lila)
    rect(50, 300, 300, 200)
    fill(0)

    # Haare im unteren Gesicht
    fill(gruen)
    luecke = 0
    for i in range(0, 5):
        triangle(100+luecke, 340, 120+luecke, 320, 140+luecke, 340)
        luecke = luecke+40

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
