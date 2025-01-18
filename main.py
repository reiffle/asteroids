import pygame #always need this, apparently
from constants import *
from player import Player #only needed Player, not whole file
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()

    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    asteroids=pygame.sprite.Group()

    Player.containers=(updatable, drawable)
    Asteroid.containers=(updatable, drawable, asteroids)
    AsteroidField.containers=updatable

    ship=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field=AsteroidField()

    dt=0

    while (1):
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for asteroid in asteroids: #I definitely didn't understand this
            if asteroid.collides_with(ship):
                print ("Game over!")
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt=clock.tick(60)/1000

main()
