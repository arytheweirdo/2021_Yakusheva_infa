import turtle as t
import math

t.shape('turtle')
t.speed(0)

w = math.sqrt(800)

n = int(input())
# v = map(int,  input().split())
v = []
for i in range(n):
    v.append(int(input()))
print(list(v))

inp = open('pochta.txt', 'r')
out = open('pochta.txt', 'w')
a = inp.readline()
out.write(a)
b = inp.readline()
out.write(b)
c = inp.readline()
out.write(c)
inp.close()
out.close()


def qw():
    t.penup()
    t.right(135)
    t.forward(40)
    t.left(90)
    t.forward(10)
    t.pendown()


for i in range(len(list(v))):
    for j in range(9):
        if a[j] == 1 and (v[i] == 1 or v[i] == 3 or v[i] == 4 or v[i] == 7 or v[i] == 9):
            t.penup()

        if a[j] == 2 and (v[i] == 2 or v[i] == 3 or v[i] == 7 or v[i] == 9):
            t.penup()

        if a[j] == 3 and (v[i] == 3 or v[i] == 5 or v[i] == 6 or v[i] == 7):
            t.penup()

        if a[j] == 4 and (v[i] == 1 or v[i] == 4 or v[i] == 6):
            t.penup()

        if a[j] == 5 and (v[i] == 1 or v[i] == 2 or v[i] == 3 or v[i] == 6 or v[i] == 7):
            t.penup()

        if a[j] == 6 and (v[i] == 1 or v[i] == 2 or v[i] == 3 or v[i] == 4 or v[i] == 5 or v[i] == 9):
            t.penup()

        if a[j] == 7 and (v[i] == 0 or v[i] == 1 or v[i] == 4 or v[i] == 5 or v[i] == 6 or v[i] == 7 or v[i] == 8):
            t.penup()

        if a[j] == 8 and (v[i] == 0 or v[i] == 1 or v[i] == 2 or v[i] == 7):
            t.penup()

        if a[j] == 9 and (v[i] == 0 or v[i] == 2 or v[i] == 4 or v[i] == 5 or v[i] == 8 or v[i] == 9):
            t.penup()

        bb = b[j]
        cc = c[j]
        t.left(bb)
        t.forward(cc)
        t.pendown()

    qw()

input()
