import pygame
import math
class Bullet:
    def __init__(self,x,y,angle):
        self.x=x
        self.y=y
        self.angle=angle
        self.radius=5
        self.vel=5
        
    def draw(self,win,colour):
        pygame.draw.circle(win,colour,(self.x,self.y),self.radius)
        
    def update(self,dt):
        self.x+=math.cos(math.radians(self.angle))*self.vel*dt
        self.y+=math.sin(math.radians(self.angle))*self.vel*dt
    