import turtle
import math

turtle.shape('turtle')
m = input("Введите начальную длину  ")
a = int(m)
h = input("Введите количество фигур")
p = int(h)-1
o = input("Введите изменение радиуса")
r = int(o)
n=4
turtle.left(60)
turtle.forward(a)
turtle.left(120)
turtle.forward(a)
turtle.left(120)
turtle.forward(a)
turtle.left(120)
turtle.right(150)
y=math.pi/3
s=2*math.sin(y)
Rad=a/s
print(math.sin(y))
print (Rad)
for i in range(p):
    y=math.pi/n
    s=math.sin(y)
    Rad=Rad+r
    a=Rad*2*s
    g=360/n
    l = g / 2
    j = 180 - l
    d=l+90
    turtle.penup()
    turtle.forward(r)
    turtle.left(d)
    for i in range(n):
        turtle.pendown()
        turtle.forward(a)
        turtle.left(g)
    n=n+1
    turtle.right(d)
    print(math.sin(y))
    print(Rad)



input()