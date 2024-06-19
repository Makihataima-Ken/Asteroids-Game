import pygame
import math
class Diraction:
    def __init__(self,ship_x,ship_y,ship_angle):
            self.distance=20
            self.radius=5
            self.x=ship_x+math.cos(math.radians(ship_angle))*self.distance
            self.y=ship_y+math.sin(math.radians(ship_angle))*self.distance
    def draw(self,win,colour):
        pygame.draw.circle(win,colour,(self.x,self.y),self.radius)
            