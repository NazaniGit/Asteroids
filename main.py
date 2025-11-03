import sys
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #INFINITE LOOP
    clock = pygame.time.Clock()
    dt = 0
    while True:
        # Handle events (so the window can close properly)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.update(dt)
        # Fill the screen with black
        screen.fill((0, 0, 0))
        # Draw Player sprite
        player.draw(screen)
        # Refresh the screen (must come last)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
