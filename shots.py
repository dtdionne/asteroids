import pygame
from circleshape import CircleShape
from constants import *
from player import *

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
          super().__init__(x, y, SHOT_RADIUS)  # Assuming CircleShape's init properly initializes position and radius.
          #self.x = x
          #self.y = y
          #self.radius = radius
          self.velocity = velocity

          #Player.shot_timer = PLAYER_SHOOT_COOLDOWN

    def draw(self, screen):
            #pygame.draw.circle(x, radius, width = 2)
            pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        #self.x += self.velocity.x * dt
        #self.y += self.velocity.y * dt
        self.position += self.velocity * dt