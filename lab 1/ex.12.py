import turtle
import math

turtle.shape('turtle')

w = input("Введите шаг ")
a = float(w)
s = input("Введите ширину линии смайлика  ")
d = int(s)
g = input("Введите ширину линии глаз  ")
t = int(g)
y = input("Введите ширину линии носа  ")
c = int(y)
o = input("Введите ширину линии рта  ")
m = int(o)
R = 360 / (2 * math.pi)
n = a / 10
l = R / 2
x = R / 3
w = 2 * x
v=a/2



def krug1():
    for i in range(360):
        turtle.forward(a)
        turtle.left(1)


def krug2():
    for i in range(360):
        turtle.forward(n)
        turtle.right(1)

def krug3():
    for i in range(180):
        turtle.forward(v)
        turtle.left(1)


def qw():
    turtle.begin_fill()
    turtle.color("blue")
    krug2()
    turtle.end_fill()
    turtle.width(t)
    turtle.color("black")
    krug2()


def qqw():
    turtle.width(c)
    turtle.color("black")
    turtle.forward(x)

def qqww():
    turtle.width(c)
    turtle.color("red")
    krug3()



turtle.left(180)

turtle.begin_fill()
turtle.color("yellow")
krug1()
turtle.end_fill()
turtle.width(d)
turtle.color("black")
krug1()
turtle.left(90)
turtle.penup()

turtle.forward(l)
turtle.right(90)
turtle.forward(x)
turtle.left(90)
turtle.pendown()
qw()
turtle.penup()
turtle.left(90)
turtle.forward(w)
turtle.left(90)
turtle.pendown()
qw()
krug2()
turtle.penup()
turtle.left(90)
turtle.forward(x)
turtle.left(90)
turtle.forward(x)
turtle.pendown()
qqw()
turtle.penup()
turtle.right(90)
turtle.forward(l)
turtle.left(90)
turtle.pendown()
qqww()




input()
