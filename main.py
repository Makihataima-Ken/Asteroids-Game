import pygame
import time
import random

WIDTH,HIGHT=1000,800
WINDOW=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Asteroids")

#Ship's properties
SHIP_X,SHIP_Y=40,60
SPEED_X,SPEED_Y=50,50
SHIP_ANGLE=90

circle_center = (WIDTH // 2, HIGHT // 2)
radius = 50
def draw():
    pygame.draw.circle(WINDOW,"blue",circle_center,radius)
    pygame.display.update()

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
        keys=pygame.key.get_pressed()
        draw()
            
    pygame.quit()

if __name__=="__main__":
    main()    