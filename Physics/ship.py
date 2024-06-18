import pygame
import math

class Ship:
    def __init__(self, x, y, angle,vel_x,vel_y):
        self.x = x
        self.y = y
        self.angle = angle
        self.vel_x=vel_x
        self.vel_y=vel_y

    def draw(self, win, colour, radius):
        pygame.draw.circle(win, colour, (self.x, self.y), radius)

    def update(self,dt,HIGHT,WIDTH):
        TURNING_VEL = 10
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_RIGHT]:
            self.angle += TURNING_VEL * dt
    
        if keys[pygame.K_LEFT]:
            self.angle-= TURNING_VEL * dt
         
        self.angle %= 2 * math.pi
    
        if keys[pygame.K_UP]:
            ship_speed = 100
            self.vel_x += math.cos(self.angle) * ship_speed * dt
            self.vel_y += math.sin(self.angle) * ship_speed * dt

        self.x += self.vel_x* dt
        self.y += self.vel_y * dt
        self.x%=WIDTH
        self.y%=HIGHT