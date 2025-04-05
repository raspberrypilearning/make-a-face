#!/bin/python3

from p5 import *
from random import randint


def sad(x_middle, y_eye, y_mouth):
    ellipse(x_middle - 50, y_eye - 20, 60, 50)  # x, y, width, height
    ellipse(x_middle + 50, y_eye - 20, 60, 50)
    ellipse(x_middle, y_mouth + 30, 100, 65)


def happy(x_middle, y_eye, y_mouth):
    ellipse(x_middle - 50, y_eye + 20, 60, 50)  # x, y, width, height
    ellipse(x_middle + 50, y_eye + 20, 60, 50)
    ellipse(x_middle, y_mouth - 30, 100, 65)


def setup():
    # Тут розмісти код, який запускається один раз
    size(400, 400)  # ширина і висота
    background(0, 0, 0)  # перемісти у draw(), щоб малюнок оновлювався на кожному кадрі
    rect_mode(CENTER)
    no_stroke()


def draw():
    # Тут розмісти код, який запускається на кожному кадрі
    mask_width = width / 2
    x_middle = width / 2
    y_eye = 180
    y_mouth = 255
    # малювання маски
    fill(255, 255, 255)  # білий
    rect(200, 150, mask_width, mask_width)
    ellipse(x_middle, 250, mask_width, 140)
    # очі та рот
    fill(0) # чорний
    ellipse(x_middle - 50, y_eye, 60, 50) # x, y, ширина, висота
    ellipse(x_middle + 50, y_eye, 60, 50)
    ellipse(x_middle, y_mouth, 100, 75)
    # частково закривати очі та рот
    fill(255)
    if mouse_x > x_middle:
        happy(x_middle, y_eye, y_mouth)
    else:
        sad(x_middle, y_eye, y_mouth)
    # закрити верхню частину маски
    fill(0)
    ellipse(x_middle, 60, 250, 90)
    # затінити половину маски
    fill(0, 25)
    rect(300, 200, width/2, height)


def mouse_pressed():
    # Тут розмісти код, який запускається при натисканні миші
    print(mouse_x, mouse_y)


# Цей рядок запускає код
run()
