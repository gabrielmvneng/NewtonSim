import pygame
from pygame.locals import *
from pygame.math import *
import sys
import physics

pygame.init()


width = 640
height = 440
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
blue = (0, 0, 255)
bg_color = (20, 20, 20)
white = (255, 255, 255)
#*arbitrary value
G = 1000

class Body:
    def __init__(self, mass, position, velocity, radius, color):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)


earth = Body(1000, Vector2(width / 2, height / 2), Vector2(10, 10), 30, blue)
moon = Body(earth.mass *0.12, Vector2(width / 3, height / 3), Vector2(-50, 70), earth.radius * 0.27, white)
bodies = [earth, moon]
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
