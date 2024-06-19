import pygame
import time
import random
import math
import Physics
import Physics.asteroids
import Physics.diraction
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


#Ship's starting point
SHIP_X,SHIP_Y=WIDTH // 2,HIGHT // 2
#players core
score =0

def draw(ship,asteroids):
    WIN.blit(BG2,(0,0))
    global score
    #draw the ship on the screen
    ship.draw(WIN,"red")
    #draw an inner circle to function as a pointer for diractions
    diraction=Physics.diraction.Diraction(ship.x,ship.y,ship.angle)
    diraction.draw(WIN,"yellow")
    #check if the bullets are released
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
    #display score
    FONT =pygame.font.SysFont("comicsans", 50)
    text = FONT.render(str(score), True,"white")
    WIN.blit(text,(0,0))
    
    #create asteroids
    for asteroid in asteroids:
        asteroid.draw(WIN)
    
    #update asteroids' state
    for asteroid in asteroids:
        asteroid.update()
        if(intersection(ship,asteroid)):
            FONT =pygame.font.SysFont("comicsans", 50)
            text = FONT.render("Game Over :(", True,"red")
            WIN.blit(text,(WIDTH/2,HIGHT/2))
            pygame.display.update()
            #pygame.time.delay(4000)
            #return 1
            
        if(asteroid.x> WIDTH or asteroid.y<0 ):
                asteroids.remove(asteroid)
        elif(asteroid.y> HIGHT or asteroid.y<0):
                asteroids.remove(asteroid)

    
    #update ship state
    ship.update(1,HIGHT,WIDTH)
    #update the display
    pygame.display.update()
    return 0
#check the condition of intersection between objects
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
        #delay asteroids' generation
        if(cnt%40==0):
            asteroids.append(Physics.asteroids.Asteroids(WIDTH,HIGHT))
            
        if(draw(ship,asteroids)):
            run=False
        
            
    pygame.quit()

if __name__=="__main__":
    main()    