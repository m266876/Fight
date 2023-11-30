import pygame
from parameters import *
import button


scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PLAY')

#button images
play_btn = pygame.image.load('../final project/sprites/1.png').convert_alpha()
exit_img = pygame.image.load('../final project/sprites/16.png').convert_alpha()
menu_img = pygame.image.load('../final project/background/homescreen.png').convert_alpha()

#button instances
play_image = button.Button(100, 50, play_btn, .5)
exit_button = button.Button(800, 100, exit_img, .5)

#loop
run = True

while run:
    scrn.blit(menu_img, (0, 0))
    if play_image.draw(scrn):
        break
    if exit_button.draw(scrn):
        pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

   # custom_font = pygame.font.Font("../final project/fonts/Black_Crayon.ttf", 48)
   # text = custom_font.render("FIGHT", True, (255, 0, 0))
   # scrn.blit(text, (SCREEN_WIDTH / 5, SCREEN_HEIGHT / 10 - text.get_height() / 2))

    pygame.display.flip()

pygame.quit()












