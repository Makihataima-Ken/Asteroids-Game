import pygame
import math
import random

rock=pygame.image.load("Asteroid.png")
Orcha=pygame.image.load("Orcha.png")
Whale=pygame.image.load("Whale.png")

class Asteroids:
    def __init__(self,width,height):
        self.x=random.random(0,width)
        self.y=random.random(0,height)
        self.angle= random.random() * (2 * math.pi)
        self.vel=2
    
    def draw(self,type,win):
        if(type==1):
            win.blit(rock,(self.x,self.y))
        elif(type==2):
             win.blit(Whale,(self.x,self.y))
        elif(type==3):
             win.blit(Orcha,(self.x,self.y))