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
yy1 = 60
xx1 = 520
xxx = 350
yyy = 70
n_number = 30
a_angle = 2 * math.pi / n_number
R1 = 40
R2 = 38
x0 = 50
y0 = 50
base_x1 = 80
base_y1 = 130
base_w1 = 90
base_h1 = 90
win_x1 = 110
win_y1 = 150
win_w1 = 30
win_h1 = 30
r1_x1 = 80
r1_y1 = 130
r2_x1 = 170
r2_y1 = 130
r3_x1 = 125
r3_y1 = 100
base_x2 = 350
base_y2 = 140
base_w2 = 60
base_h2 = 60
win_x2 = 370
win_y2 = 160
win_w2 = 20
win_h2 = 20
r1_x2 = 350
r1_y2 = 140
r2_x2 = 410
r2_y2 = 140
r3_x2 = 380
r3_y2 = 120


def draw_house(base_x, base_y, base_w, base_h, win_x, win_y, win_w, win_h, r1_x, r1_y, r2_x, r2_y, r3_x, r3_y):
    """
    Draws a house
    :param base_x: x coordinate of the base
    :param base_y: y coordinate of the base
    :param base_w: width of the base
    :param base_h: height of the base
    :param win_x: x coordinate of the window
    :param win_y: y coordinate of the window
    :param win_w: width of the window
    :param win_h: height of the window
    :param r1_x: x of the edge 1 of the roof
    :param r1_y: y of the edge 1 of the roof
    :param r2_x: x of the edge 2 of the roof
    :param r2_y: y of the edge 2 of the roof
    :param r3_x: x of the edge 3 of the roof
    :param r3_y: y of the edge 3 of the roof
    :return: None
    """
    pygame.draw.rect(screen, Tan4, (base_x, base_y, base_w, base_h))
    pygame.draw.rect(screen, Cyan4, (win_x, win_y, win_w, win_h))
    pygame.draw.polygon(screen, Firebrick4, [[r1_x, r1_y], [r2_x, r2_y], [r3_x, r3_y]])


def draw_tree(coord_x, coord_y, radius):
    """
    Draws the leaves of the tree
    :param coord_x: x coordinate of the centre
    :param coord_y: y coordinate of the centre
    :param radius: radius
    :return: None
    """
    angle = 3 / 5 * math.pi
    pygame.draw.circle(screen, Green4, (coord_x - radius / 2, coord_y + 10), 2 * radius / 3)
    pygame.draw.circle(screen, BLACK, (coord_x - radius / 2, coord_y + 10), 2 * radius / 3, 1)
    coord_x = coord_x + 10
    coord_y = coord_y + 3
    for k in range(5):
        pygame.draw.circle(screen, Green4, (coord_x, coord_y), 2 * radius / 3)
        pygame.draw.circle(screen, BLACK, (coord_x, coord_y), 2 * radius / 3, 1)
        coord_x = coord_x + radius * math.cos(angle)
        coord_y = coord_y + radius * math.sin(angle)
        angle = angle + 2 / 5 * math.pi


def draw_background():
    """
    Draws the background
    :return: None
    """
    pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, 600, 195))
    pygame.draw.rect(screen, GREEN, (0, 150, 600, 205))


def draw_sun():
    """
    Draws the sun
    :return: None
    """
    z_angle = 0
    z1_angle = 0
    pygame.draw.circle(screen, YELLOW, (x0, y0), 39)
    for i in range(n_number):
        if i == 0:
            x2 = x0 + R1 * math.cos(0)
            y2 = y0 + R1 * math.sin(0)
            x3 = x0 + R1*math.cos(a_angle)
            y3 = y0 + R1*math.sin(a_angle)
            x4 = x0 + R2*math.cos(a_angle / 2)
            y4 = y0 + R2*math.sin(a_angle / 2)
            z1_angle = a_angle / 2
            pygame.draw.aalines(screen, WHITE, False, [[x2, y2], [x4, y4], [x3, y3]])
        if i > 0:
            z_angle = z_angle + a_angle
            z1_angle = z1_angle + a_angle
            x2 = x0 + R1 * math.cos(z_angle)
            y2 = y0 + R1 * math.sin(z_angle)
            x3 = x0 + R1*math.cos(z_angle - a_angle)
            y3 = y0 + R1*math.sin(z_angle - a_angle)
            x4 = x0 + R2*math.cos(z1_angle)
            y4 = y0 + R2*math.sin(z1_angle)
            pygame.draw.aalines(screen, WHITE, False, [[x2, y2], [x4, y4], [x3, y3]])


def draw_clouds(radius, x_coordinate, y_coordinate):
    """
    Draws clouds
    :param radius: radius of the circle
    :param x_coordinate: x coordinate of the centre
    :param y_coordinate: y coordinate of the centre
    :return: None
    """
    pygame.draw.circle(screen, WHITE, (x_coordinate, y_coordinate), 2 * radius / 3)
    pygame.draw.circle(screen, BLACK, (x_coordinate, y_coordinate), 2 * radius / 3, 1)
    for j in range(6):
        if j == 1 or j == 3 or j == 5:
            x_coordinate = x_coordinate + 2 * radius / 3
        if j == 2:
            y_coordinate = y_coordinate - 2 * radius / 3
        if j == 4:
            y_coordinate = y_coordinate + 2 * radius / 3
        pygame.draw.circle(screen, WHITE, (x_coordinate, y_coordinate), 2 * radius / 3)
        pygame.draw.circle(screen, BLACK, (x_coordinate, y_coordinate), 2 * radius / 3, 1)


draw_background()
draw_house(base_x1, base_y1, base_w1, base_h1, win_x1, win_y1, win_w1, win_h1, r1_x1, r1_y1, r2_x1, r2_y1, r3_x1, r3_y1)
draw_house(base_x2, base_y2, base_w2, base_h2, win_x2, win_y2, win_w2, win_h2, r1_x2, r1_y2, r2_x2, r2_y2, r3_x2, r3_y2)

pygame.draw.rect(screen, BLACK, (230, 120, 10, 80))
draw_tree(x, y, R)
pygame.draw.rect(screen, BLACK, (480, 130, 7, 60))
draw_tree(xx, yy, Rr)

draw_clouds(R, x1, y1)
draw_clouds(R, xx1, yy1)
draw_clouds(Rr, xxx, yyy)

draw_sun()

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
