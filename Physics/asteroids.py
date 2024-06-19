import pygame
import math
import random

rock=pygame.image.load("pics\Asteroid.png")
Orcha=pygame.image.load("pics\Orcha.png")
Whale=pygame.image.load("pics\Whale.png")
scaledrock=pygame.transform.scale(rock,(70,70))
scaledorcha=pygame.transform.scale(Orcha,(140,140))
scaledwhale=pygame.transform.scale(Whale,(210,210))

class Asteroids:
    def __init__(self,width,height):
        self.rand=random.choice([[random.choice([0,width-1]),random.randint(0,height-1)],[random.randint(0,width-1),random.choice([0,height-1])]])
        self.x,self.y=self.rand
        self.angle=random.randint(0,360)
        self.vel=2
        self.type=random.randint(1,3)
        self.radius=0
    
    def draw(self,win):
        if(self.type==1):
            self.radius=70
            win.blit(scaledrock,(self.x,self.y))
        elif(self.type==2):
             self.radius=140
             win.blit(scaledwhale,(self.x,self.y))
        elif(self.type==3):
             self.radius=210
             win.blit(scaledorcha,(self.x,self.y))
             
    def update(self):
        self.x+=math.cos(math.radians(self.angle))*self.vel
        self.y+=math.sin(math.radians(self.angle))*self.vel