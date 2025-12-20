import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
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

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # Player is a LOCAL — this is the key
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000  # seconds since last frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)   # mutate state first
        log_state()          # observe state second

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
            
        pygame.display.flip()

if __name__ == "__main__":
    main()
