import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))

pygame.draw.rect(screen, (0, 191, 255),
                 (0, 0, 150, 600))
pygame.draw.rect(screen, (50, 205, 50),
                 (0, 150, 250, 600))