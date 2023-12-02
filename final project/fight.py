import pygame
from parameters import *
from players import Players


pygame.init()

scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FIGHT")

#set frame rate
clock = pygame.time.Clock()
FPS = 60


background = pygame.image.load("../final project/background/citybackground.png").convert_alpha()

#load spritesheets
gunman_sheet = pygame.image.load("../final project/sprites/gunman_spritesheet.png").convert_alpha()
zombie_sheet = pygame.image.load("../final project/sprites/zombie_spritesheet.png").convert_alpha()


#number of steps in each animation
GUNMAN_STEPS = [3,4,3,4,7,8]
ZOMBIE_STEPS = [4,5,3,4,5,7]


def draw_bg():
    scaled_bg = pygame.transform.scale(background, (1100, 600))
    scrn.blit(scaled_bg, (0,0))

#function for drawing fighter health bars
def draw_health_bar(health,x,y):
    ratio = health / 100
    pygame.draw.rect(scrn, WHITE, (x - 1, y -1, 402, 32))
    pygame.draw.rect(scrn, RED, (x, y, 400, 30))
    pygame.draw.rect(scrn, YELLOW, (x, y, 400 * ratio, 30))

#Players
gunman = Players(200, 310, False, GUNMAN_DATA, gunman_sheet, GUNMAN_STEPS)
zombie = Players(700, 310, True, ZOMBIE_DATA, zombie_sheet, ZOMBIE_STEPS)




#game loop
run = True
while run:

    clock.tick(FPS)
    #draw background
    draw_bg()

    #draw health bar
    draw_health_bar(gunman.health, 20, 20)
    draw_health_bar(zombie.health, 680, 20)

    #move players
    gunman.move(SCREEN_WIDTH, SCREEN_HEIGHT, scrn, zombie)

    #update players
    gunman.update()
    zombie.update()


    gunman.draw(scrn)
    zombie.draw(scrn)
    #draw players

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
#exit pygame
pygame.quit()
