import pygame, sys
from pygame.locals import *



pygame.init()



screen = pygame.display.set_mode((1100,750),0,32)



Running = True

while Running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            Running = False
            sys.exit()
            break



    x,y = pygame.mouse.get_pos()
    x -= screen.get_width()/2
    y -= screen.get_height()/2

    pygame.draw.rect(screen,(255,0,0),(x,y,50.50))
    pygame.display.update()
pygame.quit()
