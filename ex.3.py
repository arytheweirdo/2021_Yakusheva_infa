import pygame
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
Tan4 = (139, 90, 43)
Cyan4 = (0, 139, 139)
Firebrick4 = (139, 26, 26)
Green4 = (0, 139, 0)
x = 248
y = 110
phi = 3 / 5 * math.pi
R = 28
x1 = 150
y1 = 50
xx = 491
yy = 110
Rr = 20
yy1=60
xx1=520
xxx=350
yyy=70


pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, 600, 195))
pygame.draw.rect(screen, GREEN, (0, 150, 600, 205))

pygame.draw.rect(screen, Tan4, (80, 130, 90, 90))
pygame.draw.rect(screen, Cyan4, (110, 150, 30, 30))
pygame.draw.polygon(screen, Firebrick4, [[80, 130], [170, 130], [125, 100]])

pygame.draw.rect(screen, Tan4, (350, 140, 60, 60))
pygame.draw.rect(screen, Cyan4, (370, 160, 20, 20))
pygame.draw.polygon(screen, Firebrick4, [[350, 140], [410, 140], [380, 120]])

pygame.draw.rect(screen, BLACK, (230, 120, 10, 80))
pygame.draw.circle(screen, Green4, (x - R / 2, y + 10), 2 * R / 3)
pygame.draw.circle(screen, BLACK, (x - R / 2, y + 10), 2 * R / 3, 1)
x = x + 10
y = y + 3
for i in range(5):
    pygame.draw.circle(screen, Green4, (x, y), 2 * R / 3)
    pygame.draw.circle(screen, BLACK, (x, y), 2 * R / 3, 1)
    x = x + R * math.cos(phi)
    y = y + R * math.sin(phi)
    phi = phi + 2 / 5 * math.pi

pygame.draw.rect(screen, BLACK, (480, 130, 7, 60))
pygame.draw.circle(screen, Green4, (xx - R / 2, yy + 10), 2 * Rr / 3)
pygame.draw.circle(screen, BLACK, (xx - R / 2, yy + 10), 2 * Rr / 3, 1)
xx = xx + 10
yy = yy + 3
for i in range(5):
    pygame.draw.circle(screen, Green4, (xx, yy), 2 * Rr / 3)
    pygame.draw.circle(screen, BLACK, (xx, yy), 2 * Rr / 3, 1)
    xx = xx + Rr * math.cos(phi)
    yy = yy + Rr * math.sin(phi)
    phi = phi + 2 / 5 * math.pi


pygame.draw.circle(screen, WHITE, (x1, y1), 2 * R / 3)
pygame.draw.circle(screen, BLACK, (x1, y1), 2 * R / 3, 1)
for j in range(6):
    if j == 1 or j == 3 or j == 5:
        x1 = x1 + 2 * R / 3
    if j == 2:
        y1 = y1 - 2 * R / 3
    if j == 4:
        y1 = y1 + 2 * R / 3
    pygame.draw.circle(screen, WHITE, (x1, y1), 2 * R / 3)
    pygame.draw.circle(screen, BLACK, (x1, y1), 2 * R / 3, 1)


pygame.draw.circle(screen, WHITE, (xx1, yy1), 2 * R / 3)
pygame.draw.circle(screen, BLACK, (xx1, yy1), 2 * R / 3, 1)
for j in range(6):
    if j == 1 or j == 3 or j == 5:
        xx1 = xx1 + 2 * R / 3
    if j == 2:
        yy1 = yy1 - 2 * R / 3
    if j == 4:
        yy1 = yy1 + 2 * R / 3
    pygame.draw.circle(screen, WHITE, (xx1, yy1), 2 * R / 3)
    pygame.draw.circle(screen, BLACK, (xx1, yy1), 2 * R / 3, 1)


pygame.draw.circle(screen, WHITE, (xxx, yyy), 2 * Rr/ 3)
pygame.draw.circle(screen, BLACK, (xxx, yyy), 2 * Rr / 3, 1)
for j in range(6):
    if j == 1 or j == 3 or j == 5:
        xxx = xxx + 2 * Rr / 3
    if j == 2:
        yyy = yyy - 2 * Rr / 3
    if j == 4:
        yyy = yyy + 2 * Rr / 3
    pygame.draw.circle(screen, WHITE, (xxx, yyy), 2 * Rr / 3)
    pygame.draw.circle(screen, BLACK, (xxx, yyy), 2 * Rr / 3, 1)


n = 30
a = 2 * math.pi / n
R1 = 40
z = 0
z1 = 0
R2 = 38
x0 = 50
y0 = 50

for f in range(n):
    if i == 0:
        x2 = x0 + R1 * math.cos(0)
        y2 = y0 + R1 * math.sin(0)
        x3 = x0 + math.cos(a)
        y3 = y0 + math.sin(a)
        x4 = x0 + math.cos(a / 2)
        y4 = y0 + math.sin(a / 2)
        z1 = a / 2

    if i > 0:
        z = z + a
        z1 = z1 + a
        x2 = x0 + R1 * math.cos(z)
        y2 = y0 + R1 * math.sin(z)
        x3 = x0 + math.cos(z - a)
        y3 = y0 + math.sin(z - a)
        x4 = x0 + math.cos(z1)
        y4 = y0 + math.sin(z1)
    pygame.draw.aalines(screen, YELLOW, False, [[x2, y2], [x4, y4], [x3, y3]])



pygame.display.update()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
