import pygame
from background import *



pygame.init()

scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')


# import sprite sheet
sprite_sheet_image = pygame.image.load('../final project/sprites/Run.png').convert()

# clock object
clock = pygame.time.Clock()

RGB = (10, 150, 150)
color = (247, 247, 247)


# get images
def get_image(sheet, frame_x, frame_y, width, height):
    image = pygame.Surface((width, height)).convert()
    image.set_colorkey((color))
    image.blit(sheet, (0, 0), (frame_x * width, 0, width, height))
    return image


# loop through sprite sheet to get images
all_frames = []
idx = 0

for x in range(9):
        all_frames.insert(idx, get_image(sprite_sheet_image, x, 0, 172, 183))
        idx += 1

run = True

while run:

    # update background
    scrn.fill(city)

    # show frame image
    for x in range(len(all_frames)):
        scrn.blit(all_frames[x], (x * 75, 0))

        # uncomment these if you want to see the figure moving on the screen
        scrn.fill(RGB)
        scrn.blit(all_frames[x], (75, 0))
        pygame.display.flip()
        clock.tick(30)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()






#run = True
#while run:
 #   scrn.fill(c




#dont look down yet
#class Bullet(pygame.sprite.Sprite):
   # def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface



#hits = pygame.sprite.spritecollide(gunman, zombie, False)
#if hits:
    #run = False



#healthbar

#class HealthBar():
    #def __init__(self, x, y, w ,h, max_hp):
        #self.x = x
        #self.y = y
        #self.w = w
        #self.h = h
        #self.hp = max_hp
        #self.max_hp = max_hp

    #def draw(self,surface):
        #ratio
       # ratio = self.hp / self.max_hp
        #pygame.draw.rect(scrn, "red", (250, 250, 300, 40))
        #pygame.draw.rect(scrn, "green", (250, 250, 300 * ratio, 40))

#health_bar = HealthBar(250, 200, 300, 40, 100)
#health_bar.draw(scrn)


#max_health = 100
#health = 20
#ratio = health / max_health




#from background import *

# Initialize Pygame
#pygame.init()

# Constants
#FPS = 60

# Colors
#WHITE = (255, 255, 255)

# Player settings
#gunman_width = 40
##player_x = SCREEN_WIDTH // 2 - gunman_width // 2
#player_y = SCREEN_HEIGHT - gunman_height
#gunman_speed = 5
#jump_velocity = -15
#gravity = 1
#is_jumping = False



