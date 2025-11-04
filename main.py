import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
    
    while True:
        # Handle events (so the window can close properly)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        asteroids_list = list(asteroids)
        for i in range(len(asteroids_list)):
            for j in range(i + 1, len(asteroids_list)):
                a1 = asteroids_list[i]
                a2 = asteroids_list[j]
                if a1.collides_with(a2):
                    a1.bounce(a2)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        # Fill the screen with black
        screen.fill((0, 0, 0))
        # Draw Player sprite
        for obj in drawable:
            obj.draw(screen)
        # Refresh the screen (must come last)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
