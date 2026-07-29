import pygame
import math
from pygame.locals import *
from pygame.math import *
import sys
import physics
from constants import *

pygame.init()


width = 640
height = 440
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
blue = (0, 0, 255)
bg_color = (20, 20, 20)
white = (255, 255, 255)
red = (255, 0, 0)


class Body:
    def __init__(self, mass, position, velocity, radius, color):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)


earth = Body(EARTH_MASS, Vector2(width / 2, height / 2), Vector2(10,10), EARTH_RADIUS, blue)
moon = Body(MOON_MASS, Vector2(width / 3, height / 3), Vector2(50, 70), MOON_RADIUS, white)
mars = Body(MARS_MASS, Vector2(width / 3, height / 3 +100), Vector2(-60, -50), MARS_RADIUS, red)
bodies = [earth, moon, mars]
def main():
    running = True
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        screen.fill(bg_color)
        for body in bodies:
            body.draw(screen)
        physics.physics_update(width, height, dt, bodies, G)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
