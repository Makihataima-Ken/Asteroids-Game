import pygame
import time
import random
import math
import Physics
import Physics.ship

WIDTH,HIGHT=1000,700
WIN=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Asteroids")
BG=(pygame.image.load("BG.jpg"))
BG2=pygame.transform.scale(BG,(WIDTH,HIGHT))
asteroid=pygame.image.load("Asteroid.jpg")
spaceship=pygame.image.load("Spaceship.jpg")
Orcha=pygame.image.load("Orcha.jpg")
Whale=pygame.image.load("Whale.jpg")

#Ship's properties
SHIP_X,SHIP_Y=WIDTH // 2,HIGHT // 2
SPEED_X,SPEED_Y=50,50
SHIP_ANGLE=0

radius = 30
def draw(ship):
    WIN.blit(BG2,(0,0))
    #WIN.fill(0,0,0)

    ship.draw(WIN,"blue",radius)
    
    ship_circle_distance = 20

    POINTER_X=ship.x + math.cos(math.radians(ship.angle)) * ship_circle_distance
    POINTER_Y= ship.y + math.sin(math.radians(ship.angle)) * ship_circle_distance
    pointer_circle_center=(POINTER_X,POINTER_Y)
    pygame.draw.circle(WIN,"yellow",pointer_circle_center,5)
    ship.update(1,HIGHT,WIDTH)
    pygame.display.update()

def main():
    run=True
    
    #to manage the speed of objects in the game
    clock=pygame.time.Clock()
    ship=Physics.ship.Ship(SHIP_X,SHIP_Y,SHIP_ANGLE,SPEED_X,SPEED_Y)
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        
        draw(ship)
            
    pygame.quit()

if __name__=="__main__":
    main()    