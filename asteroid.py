import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt): #check here if not moving...might need Vector
        self.position+=self.velocity*dt
    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        angle=random.uniform(20,50)
        rock_1=self.velocity.rotate(angle) #this is a vector
        rock_2=self.velocity.rotate(-angle)
        new_radius=self.radius-ASTEROID_MIN_RADIUS
        asteroid_1=Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2=Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity=rock_1*1.2
        asteroid_2.velocity=rock_2*1.2
