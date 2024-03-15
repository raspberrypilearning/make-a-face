#!/bin/python3

from p5 import *


def setup():
    size(400, 600)
    background(255, 255, 255)
    no_stroke()


def draw():
    bleu = Color(92, 204, 206)
    vert = Color(149, 212, 122)
    rouge = Color(239, 62, 91)
    violet = Color(75, 37, 109)
    brun = Color(178, 162, 150)
    gris = Color(201, 201, 201)
    lilas = Color(160, 158, 214)

    # Fond du haut du visage
    fill(bleu)
    rect(50, 100, 300, 200)
    fill(0)

    # Cheveux du haut du visage
    fill(violet)
    ecart = 0
    for i in range(0, 5):
        triangle(100+ecart, 140, 120+ecart, 120, 140+ecart, 140)
        ecart = ecart+40

    # Haut du visage oeil gauche
    fill(gris)
    rect(80, 190, 100, 50)
    fill(rouge)
    triangle(190, 250, 70, 150, 180, 160)
    fill(vert)
    triangle(190, 250, 60, 160, 180, 170)
    fill(lilas)
    ellipse(160, 200, 30, 30)

    # Haut du visage oeil droit
    fill(gris)
    rect(220, 190, 100, 50)
    fill(rouge)
    triangle(210, 250, 330, 150, 220, 160)
    fill(vert)
    triangle(210, 250, 340, 160, 220, 170)
    fill(lilas)
    ellipse(240, 200, 30, 30)

    # Bouche du haut du visage
    fill(brun)
    rect(100, 220, 200, 50)
    fill(violet)
    rect(110, 240, 180, 10)

  # Fond du bas du visage
    fill(violet)
    rect(50, 300, 300, 200)
    fill(0)

    # Cheveux du bas du visage
    fill(vert)
    ecart = 0
    for i in range(0, 5):
        triangle(100+ecart, 340, 120+ecart, 320, 140+ecart, 340)
        ecart = ecart+40

    # Bas du visage oeil gauche
    fill(rouge)
    rect(80, 390, 100, 50)
    fill(lilas)
    triangle(190, 450, 70, 350, 180, 360)
    fill(brun)
    triangle(190, 450, 60, 360, 180, 370)
    fill(violet)
    ellipse(160, 400, 30, 30)

    # Bas du visage oeil droit
    fill(rouge)
    rect(220, 390, 100, 50)
    fill(lilas)
    triangle(210, 450, 330, 350, 220, 360)
    fill(brun)
    triangle(210, 450, 340, 360, 220, 370)
    fill(violet)
    ellipse(240, 400, 30, 30)

    # Bouche du bas du visage
    fill(vert)
    rect(100, 420, 200, 50)
    fill(rouge)
    rect(110, 440, 180, 10)


run()
