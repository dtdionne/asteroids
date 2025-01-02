import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
          super().__init__(x, y, radius)  # Assuming CircleShape's init properly initializes position and radius.
          self.x = x
          self.y = y
          self.radius = radius

    def draw(self, screen):
            #pygame.draw.circle(x, radius, width = 2)
            pygame.draw.circle(screen, "white", (int(self.x), int(self.y)), self.radius, width=2)

    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt

    #def update(self, dt):
            #return self.velocity * dt