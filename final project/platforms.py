import pygame
import random
import sys
from parameters import *

scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('image')
city = pygame.image.load("../final project/background/citybackground.png").convert()
blocks = pygame.image.load("../final project/background/blocks.png").convert()
rect = blocks.get_rect()

#create a pygame sprite class for the platforms
class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("../final project/background/blocks.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.backwards = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x,y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def oppupdate(self):
        self.x += self.backwards
        self.rect.x = self.x

    def draw(self, surf):
        surf.blit(self.image, self.rect)


platforms = pygame.sprite.Group()
