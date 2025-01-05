import pygame
from circleshape import *
from constants import *
import random
#from player import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
          super().__init__(x, y, radius)  # Assuming CircleShape's init properly initializes position and radius.
          #self.x = x
          #self.y = y
          #self.radius = radius

    def draw(self, screen):
            #pygame.draw.circle(x, radius, width = 2)
            pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        #self.x += self.velocity.x * dt
        #self.y += self.velocity.y * dt
        self.position += self.velocity * dt

    def split(self):
          old_radius = self.radius
          self.kill()
          if self.radius <= ASTEROID_MIN_RADIUS:
               return
          splitter = random.uniform(20, 50)
          first_a = self.velocity.rotate(splitter)
          second_a = self.velocity.rotate(-splitter)
          new_radius = old_radius - ASTEROID_MIN_RADIUS
          #Asteroid(self.position, new_radius, first_a * 1.2)
          #Asteroid(self.position, new_radius, second_a * 1.2)
          asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
          asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
          asteroid1.velocity = first_a * 1.2
          asteroid2.velocity = second_a * 1.2
        