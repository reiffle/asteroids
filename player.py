import pygame #hadn't imported pygame - evidently need it in all files
from constants import * #needed all constants
from circleshape import CircleShape #only needed CircleShape, not while file

class Player(CircleShape):
    def __init__(self, x, y):
        #didn't need to separately do x and y since they are in the parent
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0 #needed to make this .self

# in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation+=PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
