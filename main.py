import pygame
import time
import random
import math
import Physics
import Physics.asteroids
import Physics.ship

pygame.init()
pygame.font.init()

WIDTH,HIGHT=1000,700
WIN=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Asteroids")
BG=(pygame.image.load("pics\BG.jpg"))
BG2=pygame.transform.scale(BG,(WIDTH,HIGHT))

spaceship=pygame.image.load("pics\Spaceship.png")
scaledship=pygame.transform.scale(spaceship,(70,70))


#Ship's properties
SHIP_X,SHIP_Y=WIDTH // 2,HIGHT // 2

score =0
def draw(ship,asteroids):
    WIN.blit(BG2,(0,0))
    global score
    ship.draw(WIN,"red")
    
    ship_circle_distance = 20

    POINTER_X=ship.x + math.cos(math.radians(ship.angle)) * ship_circle_distance
    POINTER_Y= ship.y + math.sin(math.radians(ship.angle)) * ship_circle_distance
    pointer_circle_center=(POINTER_X,POINTER_Y)
    pygame.draw.circle(WIN,"yellow",pointer_circle_center,5)
    
    for bullet in ship.bullets:
            bullet.draw(WIN,"green")
            for asteroid in asteroids.copy():
                if (intersection(bullet,asteroid)):
                    score+=1
                    ship.bullets.remove(bullet)
                    if (asteroid.radius>70):
                        splitstroids=asteroid.split()
                        asteroids.append(splitstroids[0])
                        asteroids.append(splitstroids[1])
                    asteroids.remove(asteroid)
                    break
    
    FONT =pygame.font.SysFont("comicsans", 50)
    text = FONT.render(str(score), True,"white")
    WIN.blit(text,(0,0))
    
    
    for asteroid in asteroids:
        asteroid.draw(WIN)
    
    for asteroid in asteroids:
        asteroid.update()
        if(intersection(ship,asteroid)):
            FONT =pygame.font.SysFont("comicsans", 50)
            text = FONT.render("Game Over :(", True,"red")
            WIN.blit(text,(WIDTH/2,HIGHT/2))
            #pygame.time.delay(4000)
            #return 1
            
        if(asteroid.x> WIDTH or asteroid.y<0 ):
                asteroids.remove(asteroid)
        elif(asteroid.y> HIGHT or asteroid.y<0):
                asteroids.remove(asteroid)

    
    
    ship.update(1,HIGHT,WIDTH)
    pygame.display.update()
    return 0

def intersection(a, b):
        return (a.x - b.x)**2 + (a.y - b.y)**2 <= (a.radius + b.radius)**2

def main():
    run=True
    
    #to manage the speed of objects in the game
    clock=pygame.time.Clock()
    ship=Physics.ship.Ship(SHIP_X,SHIP_Y)
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
            
        if(draw(ship,asteroids)):
            run=False
        
            
    pygame.quit()

if __name__=="__main__":
    main()    