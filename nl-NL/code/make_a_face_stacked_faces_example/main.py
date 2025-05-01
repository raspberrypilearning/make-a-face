#!/bin/python3

from p5 import *


def setup():
    size(400, 600)
    background(255, 255, 255)
    no_stroke()


def draw():
    blauw = Color(92, 204, 206)
    groen = Color(149, 212, 122)
    rood = Color(239, 62, 91)
    paars = Color(75, 37, 109)
    bruin = Color(178, 162, 150)
    grijs = Color(201, 201, 201)
    lila = Color(160, 158, 214)

    # Bovenste gezicht achtergrond
    fill(blauw)
    rect(50, 100, 300, 200)
    fill(0)

    # Haar van het bovenste gezicht
    fill(paars)
    tussenruimte = 0
    for i in range(0, 5):
        triangle(100+ tussenruimte, 140, 120+ tussenruimte, 120, 140+ tussenruimte, 140)
        tussenruimte = tussenruimte+40

    # Bovenste gezicht linkeroog
    fill(grijs)
    rect(80, 190, 100, 50)
    fill(rood)
    triangle(190, 250, 70, 150, 180, 160)
    fill(groen)
    triangle(190, 250, 60, 160, 180, 170)
    fill(lila)
    ellipse(160, 200, 30, 30)

    # Bovenste gezicht rechteroog
    fill(grijs)
    rect(220, 190, 100, 50)
    fill(rood)
    triangle(210, 250, 330, 150, 220, 160)
    fill(groen)
    triangle(210, 250, 340, 160, 220, 170)
    fill(lila)
    ellipse(240, 200, 30, 30)

    # Bovenste gezicht mond
    fill(bruin)
    rect(100, 220, 200, 50)
    fill(paars)
    rect(110, 240, 180, 10)

  # Achtergrond van het onderste gezicht
    fill(paars)
    rect(50, 300, 300, 200)
    fill(0)

    # Haar van het onderste gezicht
    fill(groen)
    tussenruimte = 0
    for i in range(0, 5):
        triangle(100+tussenruimte, 340, 120+tussenruimte, 320, 140+tussenruimte, 340)
        tussenruimte = tussenruimte+40

    # Onderste gezicht linkeroog
    fill(rood)
    rect(80, 390, 100, 50)
    fill(lila)
    triangle(190, 450, 70, 350, 180, 360)
    fill(bruin)
    triangle(190, 450, 60, 360, 180, 370)
    fill(paars)
    ellipse(160, 400, 30, 30)

    # Onderste gezicht rechter oog
    fill(rood)
    rect(220, 390, 100, 50)
    fill(lila)
    triangle(210, 450, 330, 350, 220, 360)
    fill(bruin)
    triangle(210, 450, 340, 360, 220, 370)
    fill(paars)
    ellipse(240, 400, 30, 30)

    # Onderste gezicht mond
    fill(groen)
    rect(100, 420, 200, 50)
    fill(rood)
    rect(110, 440, 180, 10)


run()
