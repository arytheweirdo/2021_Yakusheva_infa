import turtle
turtle.shape('turtle')
m = input("Введите увеличение  ")
a = float(m)
s = input("Введите количество кругов  ")
d = int(s)
w = input("Введите сторону первого круга  ")
q = float(w)
turtle.left(90)
for i in range (d):
    for i in range (360):
        turtle.forward(q)
        turtle.left(1)
    for i in range(360):
        turtle.forward(q)
        turtle.right(1)

    q=q+a