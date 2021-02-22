import turtle
import math
import random


turtle.shape('turtle')
turtle.speed(0)
for i in range(100):
    turtle.forward(random.random()*100)
    turtle.left(random.random()*1000)

input()