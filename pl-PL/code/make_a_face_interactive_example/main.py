#!/bin/python3

from p5 import *
from random import randint


def sad(x_middle, y_eye, y_mouth):
    elipsa(x_middle - 50, y_eye - 20, 60, 50) # x, y, szerokość, wysokość
    elipsa(x_middle + 50, y_eye - 20, 60, 50)
    elipsa(x_middle, y_mouth + 30, 100, 65)


def szczęśliwy(x_middle, y_eye, y_mouth):
    elipsa(x_middle - 50, y_eye + 20, 60, 50) # x, y, szerokość, wysokość
    elipsa(x_middle + 50, y_eye + 20, 60, 50)
    elipsa(x_middle, y_mouth - 30, 100, 65)


def setup():
    # Wstaw kod, aby uruchomić go raz tutaj
    rozmiar(400, 400) # szerokość i wysokość
    background(0, 0, 0) # przesuń pod draw(), aby zresetować rysunek każdą klatkę
    rect_mode(CENTER)
    no_stroke()


def draw():
    # Wstaw kod, aby uruchomić każdą klatkę tutaj
    mask_width = width / 2
    x_middle = szerokość / 2
    y_oko = 180
    y_usta = 255
    # narysuj maskę
    fill(255, 255, 255) # biały
    rect(200, 150, mask_width, mask_width)
    elipsa(x_middle, 250, mask_width, 140)
    # oczy i usta
    fill(0) # czarny
    elipsa(x_middle - 50, y_eye, 60, 50) # x, y, szerokość, wysokość
    elipsa(x_middle + 50, y_eye, 60, 50)
    elipsa(x_middle, y_mouth, 100, 75)
    # częściowo zakryj oczy i usta
    fill(255)
    if mouse_x > x_middle:
        szczęśliwy(x_middle, y_eye, y_mouth)
    else:
        sad(x_middle, y_eye, y_mouth)
    # przykryj górną część maski
    fill(0)
    elipsa(x_middle, 60, 250, 90)
    # przyciemnij połowę maski
    fill(0, 25)
    rect(300, 200, width/2, height)


def mouse_pressed():
    # Wprowadź kod, który będzie uruchamiany po naciśnięciu myszy
    print(mysz_x, mysz_y)


# Zatrzymaj to, aby uruchomić swój kod
run()
