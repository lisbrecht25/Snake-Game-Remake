import pygame
import sys
import random

#CLASSES

class Button:
    def __init__(self, x, y, width, height, text='', color=(100, 100, 100), hover_color=(150, 150, 150), action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.is_hovered = False
        self.font = pygame.font.Font(None, 30)

    def draw(self, screen):
        current_color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, current_color, self.rect)
        
        if self.text:
            text_surface = self.font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)
            
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered and self.action is not None:
                if event.button == 1: 
                    self.action()
                    return True
        return False

#FUNCTIONS

def clearScreen(screen):
    screen.fill((0, 0, 0))

def showStartScreen(screen, gameTitle, titleLocation, scoreText, scoreLocation):
    screen.blit(gameTitle, titleLocation)
    scoreText = scoreFont.render("Last Score: {}".format(score), True, (255, 255, 255))
    screen.blit(scoreText, scoreLocation)
    
def spawnApple():
    appleX, appleY = random.randrange(20, 580, 20), random.randrange(20, 580, 20)
    apple = [appleX, appleY]
    pygame.draw.rect(screen, (255, 0, 0), (appleX, appleY, 20, 20))
    return apple

def spawnNewSnake(screen):
    snakeHeadX, snakeHeadY = random.randrange(60, 460, 20), random.randrange(60, 540, 20)
    snake = [[snakeHeadX, snakeHeadY], (snakeHeadX - 20, snakeHeadY), (snakeHeadX - 40, snakeHeadY)]
    for i in range(0, len(snake)):
        x, y, *_ = snake[i]
        pygame.draw.rect(screen, (0,255, 0), (x, y, 20, 20))
    return snake

def initilizeGame():
    clearScreen(screen)
    return [20, 0, 0, "right"] #[dx, dy, score, direction]

def validateAppleSpawn(appleX, appleY, snake):
    for i in range(0, len(snake)):
        x, y, *_ = snake[i]
        while x == appleX and y == appleY:
            i = 0
            appleX, appleY = random.randrange(0, 600, 20), random.randrange(0, 600, 20)
        return appleX, appleY
                      
def checkAppleCollision(screen, snake, apple, score):
    appleEaten = False
    snakeX, snakeY, *_ = snake[0]
    appleX, appleY = apple
    
    if snakeX == appleX and snakeY == appleY:
        appleX, appleY = random.randrange(0, 600, 20), random.randrange(0, 600, 20)
        appleX, appleY = validateAppleSpawn(appleY, appleX, snake)
        pygame.draw.rect(screen, (255, 0, 0), (appleX, appleY, 20, 20))
        score = score + 1
        appleEaten = True
        return score, appleX, appleY
    
    if appleEaten != True:
            lastSegement = snake.pop()
            x, y, *_ = lastSegement
            pygame.draw.rect(screen, (0, 0, 0), (x, y, 20, 20))
    return score, appleX, appleY

def checkSelfCollision(snake):
    startScreen = False
    run = True
    for i in range(1, len(snake)):
        x, y, *_ = snake[i]
        if snakeX == x and snakeY == y:
            screen.fill((0, 0, 0))
            #snakeHeadX, snakeHeadY = random.randrange(60, 460, 20), random.randrange(60, 540, 20)
            #snake = [[snakeHeadX, snakeHeadY], (snakeHeadX - 20, snakeHeadY), (snakeHeadX - 40, snakeHeadY)]
            startScreen = True
            run = False
            return startScreen, run
    return startScreen, run
            
def checkWallCollision(snake, width, height):
    snakeX, snakeY, *_ = snake[0]
    startScreen = False
    run = True
    if snakeX > width - 20 or snakeX < 0 or snakeY > height - 20 or snakeY < 0:
            screen.fill((0, 0, 0))
            startScreen = True
            run = False
            return startScreen, run
    return startScreen, run
    
# Create Screen
pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game Remake")
clock = pygame.time.Clock()

# Create state flags and initalize score
main = True
startScreen = True
run = False
score = 0

# Create text for start screen
titleFont = pygame.font.SysFont("Arial", 50)
gameTitle = titleFont.render("SNAKE GAME REMAKE", True, (255, 255, 255))
titleLocation = gameTitle.get_rect()
titleLocation.center = (width // 2, height // 3)

scoreFont = pygame.font.SysFont("Arial", 20)
scoreText = scoreFont.render("Last Score: {}".format(score), True, (255, 255, 255))
scoreLocation = scoreText.get_rect()
scoreLocation.center = (300, 300)

# Spawn initial apple and set apple flag


# Get snake head starting point and create snake from thier. Snake always starts going right.
# Draw in snake using for loop.

# Running loop of game
while main:
    while startScreen:
        showStartScreen(screen, gameTitle, titleLocation, scoreText, scoreLocation)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dx, dy, score, direction = initilizeGame()
                    snake = spawnNewSnake(screen)
                    apple = spawnApple()
                    run = True
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
        score, appleX, appleY = checkAppleCollision(screen, snake, apple, score)
        apple = [appleX, appleY]

        # Creates new location for snake head based of direction and draws it in
        snakeX = snakeX + dx
        snakeY = snakeY + dy
        snake.insert(0, (snakeX, snakeY, 20, 20))
        pygame.draw.rect(screen, (0,255, 0), (snakeX, snakeY, 20, 20))
        
        # Checks if apple has been eaten. If it has, skip removing the last segment to 'grow'
        # the snake. If no skip remove last segment and color in with black

        startScreen, run = checkSelfCollision(snake)
        if startScreen: break
        startScreen, run = checkWallCollision(snake, width, height)
        # Snake collision detector. Checks if snake hits either wall or itself.
        
        
        pygame.display.flip()
        clock.tick(10)