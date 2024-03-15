#!/bin/python3

from p5 import *
from random import randint


def triste (milieu_x, yeux_y, bouche_y) :
    ellipse(milieu_x - 50, yeux_y - 20, 60, 50) # x, y, largeur, hauteur
    ellipse(milieu_x + 50, yeux_y - 20, 60, 50)
    ellipse(milieu_x, bouche_y + 30, 100, 65)


def heureux (milieu_x, yeux_y, bouche_y) :
    ellipse(milieu_x - 50, yeux_y + 20, 60, 50) # x, y, largeur, hauteur
    ellipse(milieu_x + 50, yeux_y + 20, 60, 50)
    ellipse(milieu_x, bouche_y - 30, 100, 65)


def setup():
    # Mets le code à exécuter une fois ici
    size(400, 400) # largeur et hauteur
    background(0, 0, 0) # se déplace sous dessiner() pour réinitialiser le dessin à chaque image
    rect_mode(CENTER)
    no_stroke()


def draw():
    # Mets le code à exécuter à chaque image ici
    largeur_masque = width / 2
    milieu_x = width / 2
    yeux_y = 180
    bouche_y = 255
    # dessiner un masque
    fill(255, 255, 255)  # blanc
    rect(200, 150, masque_largeur, masque_largeur)
    ellipse(milieu_x, 250, masque_largeur, 140)
    # yeux et bouche
    fill(0)  # noir
    ellipse(milieu_x - 50, yeux_y, 60, 50) # x, y, largeur, hauteur
    ellipse(milieu_x + 50, yeux_y, 60, 50)
    ellipse(milieu_x, bouche_y, 100, 75)
    # couvrir partiellement les yeux et la bouche
    fill(255)
    if souris_x > milieu_x :
        heureux(milieu_x, yeux_y, bouche_y)
    else:
        triste(milieu_x, yeux_y, bouche_y)
    # couvrir le haut du masque
    fill(0)
    ellipse(milieu_x, 60, 250, 90)
    # ombrer la moitié du masque
    fill(0, 25)
    rect(300, 200, width/2, height)


def mouse_pressed():
    # Mets le code à exécuter lorsque la souris est pressée ici
    print (souris_x, souris_y)


# Garde ceci pour exécuter ton code
run()
