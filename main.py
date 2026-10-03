import pygame
import sys
from asteroid import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyclock = pygame.time.Clock()
    dt: float = 0.0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatable.add(player)
    drawable.add(player)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, drawable, updatable)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        if player.shot_cooldown < 0:
            player.shot_cooldown = 0
        elif player.shot_cooldown > 0:
            player.shot_cooldown -= dt
        for rock in asteroids:
            if rock.collides_with(player) == True:
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
        for shot in shots:
            for rock in asteroids:
                if shot.collides_with(rock) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    rock.kill()
        screen.fill(color="black")
        for draw_thing in drawable:
            draw_thing.draw(screen)
        pygame.display.flip()
        dt = pyclock.tick(60) / 1000


if __name__ == "__main__":
    main()
