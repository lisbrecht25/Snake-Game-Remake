import pygame
import sys

pygame.init()
Width, Height = 600, 600

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake Game Remake")
clock = pygame.time.Clock()
run = True

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.flip()
    clock.tick(60)