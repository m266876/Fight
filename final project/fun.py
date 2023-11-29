import pygame
import random
from parameters import *
from background import *
from gunman import *


pygame.init()
pygame.mixer.init()
scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FIGHT")
clock = pygame.time.Clock()


class gunman(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(sprite_sheet_image, (50,38) )
        self.image.set_colorkey((0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speedx = 0
    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_A]:
            self.speedx = -5
        if keystate[pygame.K_D]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

sprites = pygame.sprite.Group()
gunny = gunman()
sprites.add(gunny)


#score


#loopity loop loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sprites.update()

    scrn.fill(city)
    sprites.draw(scrn)
    pygame.display.flip()

pygame.mixer.music.load('../final project/sound/Runaway.mp3')

# Set the volume (optional)
pygame.mixer.music.set_volume(0.5)

# Play the music indefinitely
pygame.mixer.music.play(-1)


pygame.quit()