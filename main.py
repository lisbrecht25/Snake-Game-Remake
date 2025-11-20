import pygame
import sys
import random

pygame.init()
Width, Height = 600, 600

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake Game Remake")
clock = pygame.time.Clock()
run = True

appleX = random.randrange(20, 580, 20)
appleY = random.randrange(20, 580, 20)
pygame.draw.rect(screen, (255, 0, 0), (appleX, appleY, 20, 20))
appleSpawned = True

snakeHeadX = random.randrange(60, 540, 20)
snakeHeadY = random.randrange(60, 540, 20)
snake = [(snakeHeadX, snakeHeadY, 20, 20), (snakeHeadX - 20, snakeHeadY, 20, 20), (snakeHeadX - 40, snakeHeadY, 20, 20)]
for i in range(0, len(snake)):
    pygame.draw.rect(screen, (0,255, 0), snake[i])
direction = "right"
dx = 20
dy = 0

while run:
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                dx = 0
                dy = -20
            elif event.key == pygame.K_a:
                dx = -20
                dy = 0
            elif event.key == pygame.K_s:
                dx = 0
                dy = 20
            elif event.key == pygame.K_d:
                dx = 20
                dy = 0

    snakeHeadX, snakeHeadY, a, b = snake[0]
    snakeHeadX = snakeHeadX + dx
    snakeHeadY = snakeHeadY + dy
    snake.insert(0, (snakeHeadX, snakeHeadY, 20, 20))
    pygame.draw.rect(screen, (0, 0, 0), snake[-1])
    pygame.draw.rect(screen, (0,255, 0), snake[0])
    lastSegement = snake.pop()
    
    pygame.display.flip()
    clock.tick(10)