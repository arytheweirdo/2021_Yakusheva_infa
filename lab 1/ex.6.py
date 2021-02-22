import turtle
import math

turtle.shape('turtle')
m = input("Введите смещение  ")
a = int(m)
s = input("Введите количество кругов  ")
d = int(s)
f=d*360


fi = (2 * math.pi) / 360
k = a / (fi * 2 * math.pi)
j = fi
v = math.pow(fi, 2)
n = math.sqrt(1 + v)
b = math.log(fi + n)
L = k * (fi * n + b) / 2



turtle.pendown()
turtle.forward(L)


for i in range(f):
    fi = fi + j
    k = a / (fi * 2 * math.pi)
    v = math.pow(fi, 2)
    n = math.sqrt(1 + v)
    b = math.log(fi + n)
    L = k * (fi * n + b) / 2
    turtle.left(1)
    turtle.forward(L)
    print("в цикле", L)






input()
