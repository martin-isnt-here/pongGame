import pygame, sys, time
from pygame.locals import *

pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width, height),0,32)

pygame.display.set_caption("space invaders made for Bjørn Marcus")
psize = [50,50]

speed = 5
clock = pygame.time.Clock()




clock.tick(30)
ppos = [width/2,height/2]

pygame.time.delay(50)



p_y = 0
ppos[1] = p_y
def boundaries():
    pass

jump = False
jump_count = 10



lose = False

keys = pygame.key.get_pressed()

while not lose:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    if not(jump):
        if keys[pygame.K_w]:
            ppos[1] -= speed
        if keys[pygame.K_s]:
            ppos[1] += speed
    if keys[pygame.K_a]:
        ppos[0] -= speed
    if keys[pygame.K_d]:
        ppos[0] += speed


    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (ppos[0],ppos[1],psize[0],psize[1]))


    pygame.display.update()
pygame.quit()
