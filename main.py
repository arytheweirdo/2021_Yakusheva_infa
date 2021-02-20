import pygame as pg
import sys

sc = pg.display.set_mode((300, 300))
sc.fill((200, 255, 200))

surf1 = pg.Surface((200, 200))
surf1.fill((220, 200, 0))  # желтая
surf2 = pg.Surface((100, 100))
surf2.fill((255, 255, 255))  # белая

rect = pg.Rect((70, 20, 0, 0))

surf1.blit(surf2, rect)
sc.blit(surf1, rect)

pg.display.update()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()