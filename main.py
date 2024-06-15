import pygame
import time
import random

WIDTH,HIGHT=1000,800
WINDOW=pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Asteroids")

def main():
    run=True
    
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
    pygame.quit()

if __name__=="__main__":
    main()    