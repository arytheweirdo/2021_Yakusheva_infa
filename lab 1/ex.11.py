import turtle
import math


turtle.shape('turtle')


s = input("Введите количество спиралей  ")
d = int(s)
w = input("Введите шаг ")
R = float(w)
r=R/10


def krug():

        for i in range(180):
            turtle.forward(R)
            turtle.right(1)
        for i in range(180):
            turtle.forward(r)
            turtle.right(1)
turtle.left(90)

for i in range(d):
    krug()



input()