import turtle
import math

turtle.shape('turtle')
m = input("Введите количество вершин у звезды  ")
a = int(m)
r = input("Введите радиус описанной окружности  ")
R = int(r)
n = 360 / a  # находим угол
print(n)
yy = 179 / n
print(yy)
y = math.floor(yy)  # число вершин, умещающихся в первую половину круга
print(y)
f = y * n #общий угол для нахождения стороны и угла звезды
print(f)
fi = f*math.pi/180 #угол луча звезды
print(fi)

b=2*R*math.sin(fi/2) #сторона звезды
print(b)
turtle.penup()
turtle.backward(b/2)
turtle.pendown()

for i in range(a):
    turtle.forward(b)
    turtle.left(f)

input()

