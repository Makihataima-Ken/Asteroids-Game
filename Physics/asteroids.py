import pygame
import math
import random

rock=pygame.image.load("pics\Asteroid.png")
Orcha=pygame.image.load("pics\Orcha.png")
Whale=pygame.image.load("pics\Whale.png")


class Asteroids:
    def __init__(self,width,height):
        if(width!=None and height!=None):
            self.rand=random.choice([[random.choice([0,width-1]),random.randint(0,height-1)],[random.randint(0,width-1),random.choice([0,height-1])]])
            self.x,self.y=self.rand
        else: 
            self.x=0
            self.y=0
        self.angle=random.randint(0,360)
        self.vel=2
        self.type=random.randint(1,3)
        self.radius=70*self.type
        self.stage=self.type
    
    def draw(self,win):
        if(self.type==1):
            scaledrock=pygame.transform.scale(rock,(self.radius,self.radius))
            win.blit(scaledrock,(self.x,self.y))
        elif(self.type==2):
            scaledwhale=pygame.transform.scale(Whale,(self.radius,self.radius))
            win.blit(scaledwhale,(self.x,self.y))
        elif(self.type==3):
            scaledorcha=pygame.transform.scale(Orcha,(self.radius,self.radius))
            win.blit(scaledorcha,(self.x,self.y))
             
    def split(self):
        neostroids=[]
        n1=Asteroids(None,None)
        n1.x=self.x
        n1.y=self.y
        n1.type=self.type
        n1.radius=self.radius-70
        n2=Asteroids(None,None)
        n2.x=self.x
        n2.y=self.y
        n2.angle=(180-n1.angle)
        n2.type=self.type
        n2.radius=self.radius-70
        neostroids.append(n1)
        neostroids.append(n2)
        return neostroids
             
    def update(self):
        self.x+=math.cos(math.radians(self.angle))*self.vel
        self.y+=math.sin(math.radians(self.angle))*self.vel