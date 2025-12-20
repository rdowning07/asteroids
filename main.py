import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    # Player is a LOCAL — this is the key
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        dt = clock.tick(60) / 1000  # seconds since last frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)   # mutate state first
        log_state()          # observe state second

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
            
        pygame.display.flip()

if __name__ == "__main__":
    main()
