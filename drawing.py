import pygame, sys

pygame.init()

lose = False

width = 1000
height = 800

win = pygame.display.set_mode((width, height))

p_x=width/2
p_y=height/2
p_s=50
clock = pygame.time.Clock()

clock.tick(50)
pygame.time.delay(200)


draw = False


while not lose:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        p_x += 0.5
    if keys[pygame.K_a]:
        p_x -= 0.5
    if keys[pygame.K_w]:
        p_y -= 0.5
    if keys[pygame.K_s]:
        p_y += 0.5
    if keys[pygame.K_SPACE]:
        draw = True
    else:
        draw = False
    if keys[pygame.K_UP]:
        p_s += 0.01
    if keys[pygame.K_DOWN]:
        p_s -= 0.01

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if not draw:
        win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(p_x,p_y,p_s,p_s))
    pygame.display.update()

pygame.quit()
