import pygame
import sys
from pygame.locals import *

#init Pygame
pygame.init()

size = width,height = 600,500
speed = [-2,1]
bg = (255,255,255) # RGB

#Surface
screen = pygame.display.set_mode(size)
#set the title
pygame.display.set_caption(("I am a Robbit! I am running"))

#load the image
rabbit = pygame.image.load("1.jpg")
#get the position-rect of image
position = rabbit.get_rect()

l_head = rabbit
r_head = pygame.transform.flip(rabbit, True, False)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                rabbit = l_head
                speed = [-1,0]
            if event.key == K_RIGHT:
                rabbit = r_head
                speed = [1,0]
            if event.key == K_UP:
                speed = [0,-1]
            if event.key == K_DOWN:
                speed = [0,1]

    #move
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        #transform
        rabbit = pygame.transform.flip(rabbit, True, False)
        #move oppsite
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    #fill the bg
    screen.fill(bg)
    #update img
    screen.blit(rabbit,position)
    #update screen
    pygame.display.flip()
    #delay
    pygame.time.delay(10)

