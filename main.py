import pygame
import sys
import random

pygame.init()
Width, Height = 600, 600
dx, dy = 20, 0

# Create screen and set running flag
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake Game Remake")
clock = pygame.time.Clock()
main = True
startScreen = True
run = False

font = pygame.font.SysFont("Arial", 50)
gameTitle = font.render("SNAKE GAME REMAKE", True, (255, 255, 255))
titleLocation = gameTitle.get_rect()
titleLocation.center = (Width // 2, Height // 3)

# Spawn initial apple and set apple flag
appleX, appleY = random.randrange(20, 580, 20), random.randrange(20, 580, 20)

# Get snake head starting point and create snake from thier. Snake always starts going right.
# Draw in snake using for loop.
snakeHeadX, snakeHeadY = random.randrange(60, 460, 20), random.randrange(60, 540, 20)
snake = [[snakeHeadX, snakeHeadY], (snakeHeadX - 20, snakeHeadY), (snakeHeadX - 40, snakeHeadY)]
direction = "right"

# Running loop of game
while main:
    while startScreen:
        screen.blit(gameTitle, titleLocation)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = True
                    screen.fill((0, 0, 0))
                    for i in range(0, len(snake)):
                        x, y, *_ = snake[i]
                        pygame.draw.rect(screen, (0,255, 0), (x, y, 20, 20))
                        pygame.draw.rect(screen, (255, 0, 0), (appleX, appleY, 20, 20))
                        dx = 20
                        dy = 0
                        direction = "right"
                    startScreen = False
        pygame.display.flip()
        clock.tick(10)
    while run:
        appleEaten = False
        # Event handler. Checks for keys pressed and if exit button is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and direction != "down":
                    dx = 0
                    dy = -20
                    direction = "up"
                elif event.key == pygame.K_a and direction != "right":
                    dx = -20
                    dy = 0
                    direction = "left"
                elif event.key == pygame.K_s and direction != "up":
                    dx = 0
                    dy = 20
                    direction = "down"
                elif event.key == pygame.K_d and direction != "left":
                    dx = 20
                    dy = 0
                    direction = "right"

        # Gets snake head position from list
        snakeX, snakeY, *_ = snake[0]

        # Checks if the snake collides with the apple
        if snakeX == appleX and snakeY == appleY:
            # Gets new apple location. Then checks if new location is already filled by snake. If
            # it is a new location is generated. Then updates apple flag.
            appleX, appleY = random.randrange(0, 600, 20), random.randrange(0, 600, 20)
            for i in range(0, len(snake)):
                x, y, *_ = snake[i]
                while x == appleX and y == appleY:
                    appleX, appleY = random.randrange(0, 600, 20), random.randrange(0, 600, 20)
                    i = 0
            pygame.draw.rect(screen, (255, 0, 0), (appleX, appleY, 20, 20))
            appleEaten = True

        # Creates new location for snake head based of direction and draws it in
        snakeX = snakeX + dx
        snakeY = snakeY + dy
        snake.insert(0, (snakeX, snakeY, 20, 20))
        pygame.draw.rect(screen, (0,255, 0), (snakeX, snakeY, 20, 20))
        
        # Checks if apple has been eaten. If it has, skip removing the last segment to 'grow'
        # the snake. If no skip remove last segment and color in with black
        if appleEaten != True:
            lastSegement = snake.pop()
            x, y, *_ = lastSegement
            pygame.draw.rect(screen, (0, 0, 0), (x, y, 20, 20))

        # Snake collision detector. Checks if snake hits either wall or itself.
        for i in range(1, len(snake)):
            x, y, *_ = snake[i]
            if snakeX == x and snakeY == y:
                screen.fill((0, 0, 0))
                snakeHeadX, snakeHeadY = random.randrange(60, 460, 20), random.randrange(60, 540, 20)
                snake = [[snakeHeadX, snakeHeadY], (snakeHeadX - 20, snakeHeadY), (snakeHeadX - 40, snakeHeadY)]
                startScreen = True
                run = False
                i = 0
                break
        if snakeX > Width or snakeX < 0 or snakeY > Height or snakeY < 0:
            screen.fill((0, 0, 0))
            snakeHeadX, snakeHeadY = random.randrange(60, 460, 20), random.randrange(60, 540, 20)
            snake = [[snakeHeadX, snakeHeadY], (snakeHeadX - 20, snakeHeadY), (snakeHeadX - 40, snakeHeadY)]
            startScreen = True
            run = False
            i = 0
            break
        
        pygame.display.flip()
        clock.tick(10)