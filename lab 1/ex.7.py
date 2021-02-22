import turtle

turtle.shape('turtle')
m = input("Введите начальную длину квадрата ")
n = int(m)
a = input("Введите количество кругов")
p = int(a)

k = int(m)

turtle.forward(n)
turtle.left(90)
turtle.forward(n)
turtle.left(90)
for i in range(p):
    n=n+k
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)



input()
