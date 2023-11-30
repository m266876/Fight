import pygame
from parameters import *
import sys
import threading
import fun

pygame.init()
scrn = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Loading")

font = pygame.font.SysFont("../assets/fonts/brushed.zip", 100)

CLOCK = pygame.time.Clock()

#how many times through a for loop
WORK = 1000

#loading bar
LOADING = pygame.image.load("loadingbar.png")
LOADING_BG_RECT = LOADING.get_rect(center= (640,360))

#part that loads
loading_bar = pygame.image.load("filledloading.png")
loading_bar_rect = loading_bar.get_rect(midleft=(280,360))
loading_finished = False
loading_progress = 0
loading_bar_width = 8

def doWork():
    global loading_finished, loading_progress
    for i in range(WORK):
        loading_progress = i

    loading_finished = True

#move to game screen
    scrn.blit(fun.py)
#Thread
threading.Thread(target = doWork).start()

#loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #background
    city = pygame.image.load("../../chomp/assets/background/citybackground.png").convert()

    # Using blit to copy content from one surface to other
    scrn.blit(city, (0, 0))

    if not loading_finished:
        loading_bar_width = loading_progress / WORK * 720

        loading_bar = pygame.transform.scale(loading_bar, (int(loading_bar_width), 150))
        loading_bar_rect = loading_bar.get_rect(midleft=(280,360))

        scrn.blit(LOADING, LOADING_BG_RECT)
        scrn.blit(loading_bar, loading_bar_rect)
    else:
        #move onto game screen
        scrn.blit(fun.py)
        pygame.display.update()
    CLOCK.tick(60)
