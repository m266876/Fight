import pygame
from parameters import *

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y)::
        super(). __init__()
        self.image = pygame.Surface((50,10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x, pos_y))

    def update(self):
        self.rect.x += 5
        self.rect.opp -= 5

        if self.rect.x >= SCREEN_WIDTH + 200:
            self.kill()

        if self.rect.opp >= SCREEN_WIDTH + 200
            self.kill()