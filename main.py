import pygame
import sys
import random

pygame.init()
Width, Height = 600, 600
dx, dy = 20, 0

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake Game Remake")
clock = pygame.time.Clock()
run = True

appleX, appleY = random.randrange(20, 580, 20), random.randrange(20, 580, 20)
pygame.draw.rect(screen, (255, 0, 0), (appleX, appleY, 20, 20))
appleEaten = False

snakeHeadX, snakeHeadY = random.randrange(60, 540, 20), random.randrange(60, 540, 20)
snake = [[snakeHeadX, snakeHeadY], (snakeHeadX - 20, snakeHeadY), (snakeHeadX - 40, snakeHeadY)]
for i in range(0, len(snake)):
    x, y = snake[i]
    pygame.draw.rect(screen, (0,255, 0), (x, y, 20, 20))


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

    snakeX, snakeY, *_ = snake[0]

    if snakeX == appleX and snakeY == appleY:
        appleX, appleY = random.randrange(0, 600, 20), random.randrange(0, 600, 20)
        print(appleX, appleY)
        pygame.draw.rect(screen, (255, 0, 0), (appleX, appleY, 20, 20))
        appleEaten = True
        print("APPLE EATEN")

    snakeX = snakeX + dx
    snakeY = snakeY + dy
    snake.insert(0, (snakeX, snakeY, 20, 20))
    pygame.draw.rect(screen, (0,255, 0), (snakeX, snakeY, 20, 20))
    
    if appleEaten != True:
        lastSegement = snake.pop()
        x, y, *_ = lastSegement
        pygame.draw.rect(screen, (0, 0, 0), (x, y, 20, 20))
        print("NO APPLE EATEN")
    
    appleEaten = False
    pygame.display.flip()
    clock.tick(10)