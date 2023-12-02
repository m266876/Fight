import pygame
from parameters import *
from players import Players


pygame.init()

scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("FIGHT")

#set frame rate
clock = pygame.time.Clock()
FPS = 60

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0,0]#player scores, [gunman, zombie]
round_over = False
ROUND_OVER_COOLDOWN = 2000

background = pygame.image.load("../final project/background/citybackground.png").convert_alpha()

#load spritesheets
gunman_sheet = pygame.image.load("../final project/sprites/gunman_spritesheet.png").convert_alpha()
zombie_sheet = pygame.image.load("../final project/sprites/zombie_spritesheet.png").convert_alpha()


#number of steps in each animation
GUNMAN_STEPS = [3,4,3,4,7,8]
ZOMBIE_STEPS = [4,5,3,4,5,7]

#define font
count_font = pygame.font.Font("../final project/fonts/fightfont.ttf", 80)
score_font = pygame.font.Font("../final project/fonts/fightfont.ttf", 30)

#function for drawing text
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    scrn.blit(img, (x, y))



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
gunman = Players(1,200, 310, False, GUNMAN_DATA, gunman_sheet, GUNMAN_STEPS)
zombie = Players(2,700, 310, True, ZOMBIE_DATA, zombie_sheet, ZOMBIE_STEPS)




#game loop
run = True
while run:

    clock.tick(FPS)
    #draw background
    draw_bg()

    #draw health bar
    draw_health_bar(gunman.health, 20, 20)
    draw_health_bar(zombie.health, 680, 20)

    #update countdown
    if intro_count <= 0:
        # move players
        gunman.move(SCREEN_WIDTH, SCREEN_HEIGHT, scrn, zombie)
        zombie.move(SCREEN_WIDTH, SCREEN_HEIGHT, scrn, gunman)
    else:
        #display count timer
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        #update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()




    #update players
    gunman.update()
    zombie.update()


    #draw players
    gunman.draw(scrn)
    zombie.draw(scrn)

    #check for player defeat
    if round_over == False:
        if gunman.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif zombie.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
#exit pygame
pygame.quit()
