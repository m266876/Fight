import pygame
from background import *
import spritesheet


pygame.init()

scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('../../chomp/assets/sprites/Run.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

color1 = (0,0,0)
color2 = (0,0,0)

animation_list = []
animation_steps = [4,6,3,4]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = .5
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, color1))
        step_counter += 1
    animation_list.append(temp_img_list)
#frame_0 = sprite_sheet.get_image(0, 24, 24, 3, color1)
#frame_1 = sprite_sheet.get_image(1, 24, 24, 3, color1)
#frame_2 = sprite_sheet.get_image(2, 24, 24, 2, color1)

run = True
while run:
    scrn.fill(city)

    #animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0
    #frame image

    scrn.blit(animation_list[action][frame], (0,0))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action += 1
                frame = 0
        if event.key == pygame.K_UP and action < len(animation_list) - 1:
            action -= 1
            frame = 0


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface



hits = pygame.sprite.spritecollide(gunman, zombie, False)
if hits:
    run = False





#healthbar

class HealthBar():
    def __init__(self, x, ,y, w ,h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self,surface):
        #ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(scrn, "red", (250, 250, 300, 40))
        pygame.draw.rect(scrn, "green", (250, 250, 300 * ratio, 40))

health_bar = HealthBar(250, 200, 300, 40, 100)
health_bar.draw(scrn)


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



#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#pygame.display.set_caption("Run")

# import sprite sheet
#sprite_sheet_image = pygame.image.load('Run.png').convert()

# clock object
#clock = pygame.time.Clock()

#RGB = (10, 150, 150)
#color = (247, 247, 247)


# get images
#def get_image(sheet, frame_x, frame_y, width, height, scale, color):
 #   image = pygame.Surface((width, height)).convert()
  #  image.set_colorkey((color))
  #  image.blit(sheet, (0, 0), (frame_x * width, frame_y * height, width, height))
  #  image = pygame.transform.scale(image, (width * scale, height * scale))
   # return image


# loop through sprite sheet to get images
#all_frames = []
#idx = 0

#for x in range(5):
  #  for y in range(2):
      #  all_frames.insert(idx, get_image(sprite_sheet_image, x, y, 172, 183, .5, color))
       # idx += 1

#run = True

#while run:

    # update background
  #  screen.fill(RGB)

    # show frame image
  #  for x in range(len(all_frames)):
   #     screen.blit(all_frames[x], (x * 75, 0))

        # uncomment these if you want to see the figure moving on the screen
     #   screen.fill(RGB)
      #  screen.blit(all_frames[x], (75, 0))
       # pygame.display.flip()
        #clock.tick(30)

    # event handler
 #   for event in pygame.event.get():
     #   if event.type == pygame.QUIT:
        #    run = False

#pygame.display.flip()

#pygame.quit()
