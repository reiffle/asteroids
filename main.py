import pygame #always need this, apparently
from constants import *
from player import Player #only needed Player, not whole file

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    ship=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt=0
    while (1):
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                return
        ship.update(dt)
        screen.fill("black")
        ship.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000

main()
