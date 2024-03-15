#!/bin/python3

from p5 import *


def setup():
    size(400, 600)
    background(255, 255, 255)
    no_stroke()


def draw():
    Niebieski = Kolor(92, 204, 206)
    Zielony = Kolor(149, 212, 122)
    Czerwony = Kolor(239, 62, 91)
    Fioletowy = Kolor(75, 37, 109)
    Brązowy = Kolor(178, 162, 150)
    Szary = Kolor(201, 201, 201)
    Liliowy = Kolor(160, 158, 214)

    # Tło górnej twarzy
    fill(niebieski)
    rect(50, 100, 300, 200)
    fill(0)

    # Włosy na wierzchu
    fill(fioletowy)
    przerwa = 0
    for i in range(0, 5):
        trójkąt(100+gap, 140, 120+gap, 120, 140+gap, 140)
        przerwa = przerwa+40

    # Górna twarz Lewe oko
    fill(szary)
    rect(80, 190, 100, 50)
    fill(czerwony)
    triangle(190, 250, 70, 150, 180, 160)
    fill(zielony)
    triangle(190, 250, 60, 160, 180, 170)
    fill(liliowy)
    ellipse(160, 200, 30, 30)

    # Górna twarz prawego oka
    fill(szary)
    rect(220, 190, 100, 50)
    fill(czerwony)
    triangle(210, 250, 330, 150, 220, 160)
    fill(zielony)
    triangle(210, 250, 340, 160, 220, 170)
    fill(liliowy)
    ellipse(240, 200, 30, 30)

    # Usta górnej twarzy
    fill(brązowy)
    rect(100, 220, 200, 50)
    fill(fioletowy)
    rect(110, 240, 180, 10)

  # Dolna twarz tła
    fill(fioletowy)
    rect(50, 300, 300, 200)
    fill(0)

    # Dolna twarz włosy
    fill(zielony)
    przerwa = 0
    for i in range(0, 5):
        trójkąt(100+gap, 340, 120+gap, 320, 140+gap, 340)
        przerwa = przerwa+40

    # Dolna ściana Lewe oko
    fill(czerwony)
    rect(80, 390, 100, 50)
    fill(liliowy)
    triangle(190, 450, 70, 350, 180, 360)
    fill(brązowy)
    triangle(190, 450, 60, 360, 180, 370)
    fill(fioletowy)
    ellipse(160, 400, 30, 30)

    # Dolna twarz prawego oka
    fill(czerwony)
    rect(220, 390, 100, 50)
    fill(liliowy)
    triangle(210, 450, 330, 350, 220, 360)
    fill(brązowy)
    triangle(210, 450, 340, 360, 220, 370)
    fill(fioletowy)
    ellipse(240, 400, 30, 30)

    # Usta dolnej twarzy
    fill(zielony)
    rect(100, 420, 200, 50)
    fill(czerwony)
    rect(110, 440, 180, 10)


run()
