import pygame
import time
import random
import math
import Physics

WIDTH,HIGHT=1000,700
WIN=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Asteroids")
#BG=pygame.image.load("AsteroidsBackground.jpg")

#Ship's properties
SHIP_X,SHIP_Y=WIDTH // 2,HIGHT // 2
SPEED_X,SPEED_Y=50,50
SHIP_ANGLE=0

ship_circle_center = (SHIP_X,SHIP_Y)
radius = 30
def draw():
    #WIN.blit(BG,(0,0))
    WIN.fill(0,0,0)
    pygame.draw.circle(WIN,"blue",ship_circle_center,radius)
    
    
    
    ship_circle_distance = 20

    POINTER_X=SHIP_X + math.cos(SHIP_ANGLE) * ship_circle_distance
    POINTER_Y= SHIP_Y + math.sin(SHIP_ANGLE) * ship_circle_distance
    pointer_circle_center=(POINTER_X,POINTER_Y)
    pygame.draw.circle(WIN,"yellow",pointer_circle_center,5)
    
    pygame.display.update()

def update(dt):
    global SHIP_ANGLE
    global SHIP_X
    global SHIP_Y
    global SPEED_X
    global SPEED_Y
    
    TURNING_VEL = 10
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        SHIP_ANGLE += TURNING_VEL * dt
    
    if keys[pygame.K_LEFT]:
        SHIP_ANGLE -= TURNING_VEL * dt
        
    SHIP_ANGLE %= 2 * math.pi
    
    if keys[pygame.K_UP]:
        ship_speed = 100
        SPEED_X += math.cos(SHIP_ANGLE) * ship_speed * dt
        SPEED_Y += math.sin(SHIP_ANGLE) * ship_speed * dt

    SHIP_X += SPEED_X * dt
    SHIP_Y += SPEED_Y * dt
    SHIP_X%=WIDTH
    SHIP_Y%=HIGHT
    
def main():
    run=True
    
    #to manage the speed of objects in the game
    clock=pygame.time.Clock()
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        draw()
            
    pygame.quit()

if __name__=="__main__":
    main()    