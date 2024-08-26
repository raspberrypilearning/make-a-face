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
    helllila = Color(160, 158, 214)

    # Top face background
    fill(blau)
    rect(50, 100, 300, 200)
    fill(0)

    # Top face Hair
    fill(helllila)
    luecke = 0
    for i in range(0, 5):
        triangle(100+luecke, 140, 120+luecke, 120, 140+luecke, 140)
        luecke = luecke+40

    # Top face Left Eye
    fill(gruen)
    rect(80, 190, 100, 50)
    fill(rot)
    triangle(190, 250, 70, 150, 180, 160)
    fill(gruen)
    triangle(190, 250, 60, 160, 180, 170)
    fill(lila)
    ellipse(160, 200, 30, 30)

    # Top face Right Eye
    fill(gruen)
    rect(220, 190, 100, 50)
    fill(rot)
    triangle(210, 250, 330, 150, 220, 160)
    fill(helllila)
    triangle(210, 250, 340, 160, 220, 170)
    fill(lila)
    ellipse(240, 200, 30, 30)

    # Top face Mouth
    fill(braun)
    rect(100, 220, 200, 50)
    fill(helllila)
    rect(110, 240, 180, 10)

  # Bottom face background
    fill(grau)
    rect(50, 300, 300, 200)
    fill(0)

    # Bottom face Hair
    fill(lila)
    luecke = 0
    for i in range(0, 5):
        triangle(100+luecke, 340, 120+luecke, 320, 140+luecke, 340)
        luecke = luecke+40

    # Bottom face Left Eye
    fill(rot)
    rect(80, 390, 100, 50)
    fill(lila)
    triangle(190, 450, 70, 350, 180, 360)
    fill(braun)
    triangle(190, 450, 60, 360, 180, 370)
    fill(grau)
    ellipse(160, 400, 30, 30)

    # Bottom face Right Eye
    fill(rot)
    rect(220, 390, 100, 50)
    fill(lila)
    triangle(210, 450, 330, 350, 220, 360)
    fill(braun)
    triangle(210, 450, 340, 360, 220, 370)
    fill(helllila)
    ellipse(240, 400, 30, 30)

    # Bottom face Mouth
    fill(gruen)
    rect(100, 420, 200, 50)
    fill(rot)
    rect(110, 440, 180, 10)


run()
