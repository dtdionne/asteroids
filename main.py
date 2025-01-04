# this allows us to use code from
 # the open-source pygame library
  # throughout this file
import pygame, circleshape, sys
from constants import *
from player import *
from circleshape import CircleShape
from asteroids import *
from asteroidfield import *
from shots import *
   
def main():
       print("Starting asteroids!")
       print(f"Screen width: {SCREEN_WIDTH}")
       print(f"Screen height: {SCREEN_HEIGHT}")
       pygame.init()
       clock = pygame.time.Clock()
       dt = 0
       screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
       color = (0,0,0)
       x = SCREEN_WIDTH / 2
       y = SCREEN_HEIGHT / 2
       updatable = pygame.sprite.Group()
       drawable = pygame.sprite.Group()
       asteroids = pygame.sprite.Group()
       shots = pygame.sprite.Group()
       #collisions = pygame.sprite.Group()
       #asteroidfield = pygame.sprite.Group() 
       Player.containers = (updatable, drawable)
       Asteroid.containers = (asteroids, updatable, drawable)
       AsteroidField.containers = (updatable)
       Shot.containers = (shots, updatable, drawable)
       #collisions.containers = (updatable)
       player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
       asteroidfield = AsteroidField()
       #player.shoot()
       #collisions = CircleShape(collisions)
       #player.updatable = (group_a, group_b)
       #player.drawable = (group_a, group_b)
       #updatable = pygame.sprite.Group()
       #drawable = pygame.sprite.Group()
       #Player.containers = (updatable, drawable)
       while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color)
        for i in updatable:
              i.update(dt)
        for asteroid in asteroids:
              if player.collision(asteroid):
                   sys.exit("Game over!")
              for shot in shots:
                   if shot.collision(asteroid):
                        asteroid.kill()
        for i in drawable:
              i.draw(screen)
        #player.draw(screen)
        #player.update(dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
            main()
