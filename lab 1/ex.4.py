import turtle as t
t.shape('turtle')
a=10
c=5
for i in range(10):
    t.pendown()
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.right(90)
    t.backward(a)

    a=a+10
    t.penup()
    t.backward(c)
    t.left(90)
    t.forward(c)
    t.right(180)







input()