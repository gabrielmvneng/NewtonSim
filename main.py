import pygame
from pygame.locals import *
from pygame.math import *
import sys

pygame.init()

width = 640
height = 440
screen = pygame.display.set_mode((width, height))
running = True
clock = pygame.time.Clock()
blue = (0, 0, 255)
bg_color = (20, 20, 20)

class Body:
    def __init__(self, mass, position, velocity, radius, color):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def physics_update(self, dt):
        self.position += self.velocity * dt

earth = Body(6 * 10**24, Vector2(width / 2, height / 2), Vector2(90, 90), 30, blue)
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    earth.physics_update(dt)
    screen.fill(bg_color)
    earth.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()