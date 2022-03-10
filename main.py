from turtle import Turtle, Screen, colormode
import random

colors = [
    (236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15),
    (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168),
    (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
    (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199),
    (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232),
    (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199),
    (179, 17, 8), (233, 66, 34)
]
x = -290
y = -220

colormode(255)
tim = Turtle()
tim.speed(0)
tim.up()
tim.hideturtle()

for _ in range(10):
    tim.setx(x)
    tim.sety(y)
    for _ in range(10):
        tim.fd(50)
        tim.dot(20, random.choice(colors))
    y = y + 50

screen = Screen()
screen.exitonclick()
