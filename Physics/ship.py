import pygame
import math

class Ship:
    def __init__(self, x, y, angle,vel_x,vel_y):
        self.x = x
        self.y = y
        self.angle = angle
        self.vel_x=vel_x
        self.vel_y=vel_y
        self.bullets=[]
        self.radius=30

    def draw(self, win, colour):
        pygame.draw.circle(win, colour, (self.x, self.y), self.radius)

    def update(self,dt,HIGHT,WIDTH):
        TURNING_VEL = 10
        keys = pygame.key.get_pressed()
    
        #Diractions
        if keys[pygame.K_RIGHT]:
            self.angle += TURNING_VEL * dt
    
        if keys[pygame.K_LEFT]:
            self.angle-= TURNING_VEL * dt
         
        #self.angle %= 2 * math.pi
        
        #Movment
        if keys[pygame.K_UP]:
            ship_speed = 2
            self.vel_x = math.cos(math.radians(self.angle)) * ship_speed * dt
            self.vel_y = math.sin(math.radians(self.angle)) * ship_speed * dt
        #update position
        self.x += self.vel_x* dt
        self.y += self.vel_y * dt
        self.x%=WIDTH
        self.y%=HIGHT
        
        #bullets control
        for bullet in self.bullets:
            bullet_speed = 5
            bullet['x'] += math.cos(bullet['angle']) * bullet_speed * dt
            bullet['y'] += math.sin(bullet['angle']) * bullet_speed * dt
            if(bullet['x']> WIDTH or bullet['x']<0 ):
                self.bullets.remove(bullet)
            elif(bullet['y']> HIGHT or bullet['y']<0):
                self.bullets.remove(bullet)
            
        
        if keys[pygame.K_s]:
            self.bullets.append({'x': self.x+math.cos(math.radians(self.angle)),
                                 'y': self.y+math.sin(math.radians(self.angle)),
                                 'angle': self.angle,
                                 })