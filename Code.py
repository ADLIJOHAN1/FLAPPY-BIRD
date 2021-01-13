import pygame
import random
import sys

pygame.init()

#BACKGROUND, ICON AND TITLE 
display=pygame.display.set_mode((576,1024))
icon=pygame.image.load("favicon.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("Flappy Bird")

#BACKGROUND
background=pygame.image.load("sprites/background-night.png").convert()
clock=pygame.time.Clock()

#FLOOR
floor1=pygame.image.load("sprites/base.png").convert()
floor1_position=0
floor2_position=576
floor2=pygame.image.load("sprites/base.png").convert()
floor_position_change=1

#BIRD
bird=pygame.image.load("sprites/yellowbird-midflap.png").convert_alpha()
bird_x=int(200)
bird_y=int(512)
bird_rectangle=bird.get_rect(center = (bird_x,bird_y))
gravity = 0.5



#GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE:
               bird_x+=12
               bird_y-=12
        bird_x+=gravity
        bird_y+=gravity
        floor1_position-=floor_position_change
        floor2_position-=floor_position_change
        if floor2_position<10:
            floor1_position = 0
            floor2_position = 576
    display.blit(background,(0,0))
    display.blit(floor1,(floor1_position,832))
    display.blit(floor2,(floor2_position,832))
    display.blit(bird,(bird_x,bird_y))
    pygame.display.update()
    clock.tick(120)
