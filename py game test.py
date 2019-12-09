
import random, sys, pygame
import os


width=500
height=500

px=width/2
py=height/2
ps=50

scr=pygame.display.set_mode((width, height))

player1=[50, 50]
player1cor=[width/2, height/2]
img=pygame.image.load(os.path.join(r"C:\Users\henry\Desktop\Games made by me", "kappaRAINBOW.png"))


lose=False

keys=pygame.key.get_pressed()

while not lose:

    if keys[K_w]:
        py -= ps


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    scr.blit(img,(0,0))






pygame.update()
