import pygame #hadn't imported pygame - evidently need it in all files
from constants import * #needed all constants
from circleshape import CircleShape #only needed CircleShape, not while file
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        #didn't need to separately do x and y since they are in the parent
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0 #needed to make this self.rotation
        self.timer=PLAYER_SHOOT_COOLDOWN

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
        self.timer-=dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot (self): #Look at this to understand what's happening
        if (self.timer<=0):
            bullet=Shot(self.position.x, self.position.y)
            bullet.velocity=pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            self.timer=PLAYER_SHOOT_COOLDOWN

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
