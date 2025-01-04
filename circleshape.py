import pygame
#from player import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    #def collision(self, rock):
    #    self.distance = rock.radius + self.radius
    #    #self.col = self.position + rock.position
    #    self.col = self.position.distance_to(rock.position)
    #    return self.distance <= self.col

    def collision(self, rock):
        total_radius = rock.radius + self.radius  # sum of both radii
        actual_distance = self.position.distance_to(rock.position)
        return actual_distance <= total_radius

    def draw(self, screen):
        #pygame.draw.polygon(screen, "white", self.triangle(), 2)
        pass


    def update(self, dt):
        # sub-classes must override
        pass




#detected = pygame.Vector2()
