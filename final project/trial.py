import pygame
import sys

from home import homescreen

pygame.init()
#scrn = pygame.display.set_mode((600, 600))
#pygame.display.set_caption("TEST")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        homescreen()


    pygame.display.flip()

