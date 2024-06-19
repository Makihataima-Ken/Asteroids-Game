import pygame
import time
import random
import math
import Physics
import Physics.asteroids
import Physics.ship

pygame.init()

WIDTH,HIGHT=1000,700
WIN=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Asteroids")
BG=(pygame.image.load("BG.jpg"))
BG2=pygame.transform.scale(BG,(WIDTH,HIGHT))

spaceship=pygame.image.load("Spaceship.png")
scaledship=pygame.transform.scale(spaceship,(70,70))


#Ship's properties
SHIP_X,SHIP_Y=WIDTH // 2,HIGHT // 2
SPEED_X,SPEED_Y=0,0
SHIP_ANGLE=0

def draw(ship,asteroids):
    WIN.blit(BG2,(0,0))
    #WIN.fill(0,0,0)
    
    ship.draw(WIN,"red")
    
    ship_circle_distance = 20

    POINTER_X=ship.x + math.cos(math.radians(ship.angle)) * ship_circle_distance
    POINTER_Y= ship.y + math.sin(math.radians(ship.angle)) * ship_circle_distance
    pointer_circle_center=(POINTER_X,POINTER_Y)
    pygame.draw.circle(WIN,"yellow",pointer_circle_center,5)
    
    for bullet in ship.bullets:
               pygame.draw.circle(WIN,"green",(bullet['x']-(ship.radius/2), bullet['y']-(ship.radius/2)),5)
    
    for asteroid in asteroids:
        asteroid.draw(WIN)
    
    for asteroid in asteroids:
        asteroid.update()
        if(intersection(ship,asteroid)):
            print("collision")
        if(asteroid.x> WIDTH or asteroid.y<0 ):
                asteroids.remove(asteroid)
        elif(asteroid.y> HIGHT or asteroid.y<0):
                asteroids.remove(asteroid)

    
    
    ship.update(1,HIGHT,WIDTH)
    pygame.display.update()

def intersection(a, b):
        return (a.x - b.x)**2 + (a.y - b.y)**2 <= (a.radius + b.radius)**2

def main():
    run=True
    
    #to manage the speed of objects in the game
    clock=pygame.time.Clock()
    ship=Physics.ship.Ship(SHIP_X,SHIP_Y,SHIP_ANGLE,SPEED_X,SPEED_Y)
    asteroids=[]
    cnt=0
    while run:
        clock.tick(60)
        cnt+=1
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        if(cnt%40==0):
            asteroids.append(Physics.asteroids.Asteroids(WIDTH,HIGHT))
            
        draw(ship,asteroids)
            
    pygame.quit()

if __name__=="__main__":
    main()    