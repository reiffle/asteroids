import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y): #Need to pass in x,y, coordinates, but not radius
        super().__init__(x,y,SHOT_RADIUS) #initiate radius here

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    def update(self, dt): #check here if not moving...might need Vector
        self.position+=self.velocity*dt


