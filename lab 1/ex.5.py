import turtle
turtle.shape('turtle')

m = input ("Введите количество лап у паука ")
n=int(m)
c=360/n

for i in range(n):
    turtle.forward(60)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(60)
    turtle.left(180)
    turtle.left(c)



