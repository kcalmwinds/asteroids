import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyclock = pygame.time.Clock()
    dt: float = 0.0
    ##print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    ##print(f"Screen width: {SCREEN_WIDTH}")
    ##print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()
        dt = pyclock.tick(60) / 1000


if __name__ == "__main__":
    main()
