#!/bin/python3

from p5 import *
from random import randint


def traurig(x_mitte, y_auge, y_mund):
    ellipse(x_mitte - 50, y_auge - 20, 60, 50)  # x, y, Breite, Höhe
    ellipse(x_mitte + 50, y_auge - 20, 60, 50)
    ellipse(x_mitte, y_mund + 30, 100, 65)


def gluecklich(x_mitte, y_auge, y_mund):
    ellipse(x_mitte - 50, y_auge + 20, 60, 50)  # x, y, Breite, Höhe
    ellipse(x_mitte + 50, y_auge + 20, 60, 50)
    ellipse(x_mitte, y_mund - 30, 100, 65)


def setup():
    # Füge hier den Code ein, der einmal ausgeführt werden soll
    size(400, 400)  # Breite und Höhe
    background(0, 0, 0)  # verschiebe unter draw(), um die Zeichnung jeden Frame zurückzusetzen
    rect_mode(CENTER)
    no_stroke()


def draw():
    # Füge hier den Code ein, der bei jedem Frame ausgeführt werden soll
    masken_breite = width / 2
    x_mitte = width / 2
    y_auge = 180
    y_mund = 255
    # Maske zeichnen
    fill(255, 255, 255)  # Weiß
    rect(200, 150, masken_breite, masken_breite)
    ellipse(x_mitte, 250, masken_breite, 140)
    # Augen und Mund
    fill(0)  # Schwarz
    ellipse(x_mitte - 50, y_auge, 60, 50)  # x, y, Breite, Höhe
    ellipse(x_mitte + 50, y_auge, 60, 50)
    ellipse(x_mitte, y_mund, 100, 75)
    # Augen und Mund teilweise abdecken
    fill(255)
    if mouse_x > x_mitte:
        gluecklich(x_mitte, y_auge, y_mund)
    else:
        traurig(x_mitte, y_auge, y_mund)
    # oberen Teil der Maske abdecken
    fill(0)
    ellipse(x_mitte, 60, 250, 90)
    # Hälfte der Maske schattieren
    fill(0, 25)
    rect(300, 200, width/2, height)


def mouse_pressed():
    # Füge hier den Code ein, der ausgeführt werden soll, wenn die Maustaste gedrückt wird
    print(mouse_x, mouse_y)


# Lass dies so stehen, um deinen Code auszuführen
run()
