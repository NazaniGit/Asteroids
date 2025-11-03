from constants import *
import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    #INFINITE LOOP
    while True:
        # Handle events (so the window can close properly)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Refresh the screen (must come last)
        pygame.display.flip()

if __name__ == "__main__":
    main()
