#!/bin/python3

from p5 import *
from random import randint


def triste(x_meio, y_olho, y_boca):
    ellipse(x_meio - 50, y_olho - 20, 60, 50) # x, y, largura, altura
    ellipse(x_meio + 50, y_olho - 20, 60, 50)
    ellipse(x_meio, y_boca + 30, 100, 65)


def feliz(x_meio, y_olho, y_boca):
    ellipse(x_meio - 50, y_olho + 20, 60, 50) # x, y, largura, altura
    ellipse(x_meio + 50, y_olho + 20, 60, 50)
    ellipse(x_meio, y_boca - 30, 100, 65)


def setup():
    # Coloque o código para ser executado uma vez aqui
    size(400, 400) # largura e altura
    background(0, 0, 0) # mova em draw() para redefinir o desenho a cada quadro
    rect_mode(CENTER)
    no_stroke()


def draw():
    # Coloque o código para executar em cada quadro aqui
    largura_máscara = width / 2
    x_meio = width / 2
    y_olho = 180
    y_boca = 255
    # desenhe a máscara
    fill(255, 255, 255) # branco
    rect(200, 150, largura_máscara, largura_máscara)
    ellipse(x_meio, 250, largura_máscara, 140)
    # olhos e boca
    fill(0) # preto
    ellipse(x_meio - 50, y_olho, 60, 50) # x, y, largura, altura
    ellipse(x_meio + 50, y_olho, 60, 50)
    ellipse(x_meio, y_boca, 100, 75)
    # cubra parcialmente os olhos e a boca
    fill(255)
    if mouse_x > x_meio:
        feliz(x_meio, y_olho, y_boca)
    else:
        triste(x_meio, y_olho, y_boca)
    #cobre a parte superior da máscara
    fill(0)
    ellipse(x_meio, 60, 250, 90)
    # sombreie metade da máscara
    fill(0, 25)
    rect(300, 200, width/2, height)


def mouse_pressed():
    # Coloque o código para ser executado quando o mouse for pressionado aqui
    print(mouse_x, mouse_y)


# Mantenha isto para executar seu código
run()
