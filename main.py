import pygame
from pygame.locals import *
from pygame.math import *
import sys

pygame.init()

screen = pygame.display.set_mode((640, 340))
running = True
clock = pygame.time.Clock()

class Body:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

Earth = Body(6 * 10**24, Vector2(0, 0), Vector2(0, 0))
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    pygame.display.update()

pygame.quit()
sys.exit()