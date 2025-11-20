import pygame

class Snake():
    def __init__(self, speed):
        self.speed = speed

    def spawnSnake(self):
        self.snakePos = []
