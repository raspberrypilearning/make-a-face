#!/bin/python3

from p5 import *


def setup():
    size(400, 600)
    background(255, 255, 255)
    no_stroke()


def draw():
    azul = Color(92, 204, 206)
    verde = Color(149, 212, 122)
    vermelho = Color(239, 62, 91)
    roxo = Color(75, 37, 109)
    marrom = Color(178, 162, 150)
    cinza = Color(201, 201, 201)
    lilas = Color(160, 158, 214)

    # Fundo do rosto superior
    fill(azul)
    rect(50, 100, 300, 200)
    fill(0)

    # Cabelo do rosto superior
    fill(roxo)
    gap = 0
    for i in range(0, 5):
        triangle(100+gap, 140, 120+gap, 120, 140+gap, 140)
        gap = gap+40

    # Olho esquerdo no rosto superior
    fill(cinza)
    rect(80, 190, 100, 50)
    fill(vermelho)
    triangle(190, 250, 70, 150, 180, 160)
    fill(verde)
    triangle(190, 250, 60, 160, 180, 170)
    fill(lilas)
    ellipse(160, 200, 30, 30)

    # Olho direito do rosto superior
    fill(cinza)
    rect(220, 190, 100, 50)
    fill(vermelho)
    triangle(210, 250, 330, 150, 220, 160)
    fill(verde)
    triangle(210, 250, 340, 160, 220, 170)
    fill(lilas)
    ellipse(240, 200, 30, 30)

    # Boca do rosto superior
    fill(marrom)
    rect(100, 220, 200, 50)
    fill(roxo)
    rect(110, 240, 180, 10)

  # Fundo do rosto inferior
    fill(roxo)
    rect(50, 300, 300, 200)
    fill(0)

    # Cabelo do rosto inferior
    fill(verde)
    gap = 0
    for i in range(0, 5):
        triangle(100+gap, 340, 120+gap, 320, 140+gap, 340)
        gap = gap+40

    # Olho esquerdo do rosto inferior
    fill(vermelho)
    rect(80, 390, 100, 50)
    fill(lilas)
    triangle(190, 450, 70, 350, 180, 360)
    fill(marrom)
    triangle(190, 450, 60, 360, 180, 370)
    fill(roxo)
    ellipse(160, 400, 30, 30)

    # Olho direito do rosto inferior
    fill(vermelho)
    rect(220, 390, 100, 50)
    fill(lilas)
    triangle(210, 450, 330, 350, 220, 360)
    fill(marrom)
    triangle(210, 450, 340, 360, 220, 370)
    fill(roxo)
    ellipse(240, 400, 30, 30)

    # Boca do rosto inferior
    fill(verde)
    rect(100, 420, 200, 50)
    fill(vermelho)
    rect(110, 440, 180, 10)


run()
