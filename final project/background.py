import pygame
from parameters import *
from platforms import *

# Activate the pygame library.
pygame.init()


city = pygame.image.load("../final project/background/citybackground.png").convert()
blocks = pygame.image.load("../final project/background/blocks.png").convert()
rect = blocks.get_rect()
#
scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Draw the city background
scrn.blit(city, (0, 0))

def draw_background(surface):
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        surface.blit(blocks, (x, SCREEN_HEIGHT - TILE_SIZE))


def add_platforms(num_plat):
    for _ in range(num_plat):
        platforms.add(Platforms(random.randint(0, SCREEN_WIDTH - 10),
                        random.randint(TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE)))

#platforms.draw(scrn)


# Draw the background
draw_background(scrn)
platforms.draw(scrn)


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Draw the text

    #custom_font = pygame.font.Font("../../chomp/assets/fonts/brushed.zip", 48)
    #text = custom_font.render("FIGHT", True, (255, 0, 0))
    #scrn.blit(text, (SCREEN_WIDTH / 5, SCREEN_HEIGHT / 10 - text.get_height() / 2))

    # Update the display
    pygame.display.flip()

# Deactivate the pygame library
pygame.quit()
















# importing required library


#import pygame
#from parameters import *
# activate the pygame library .
#pygame.init()
#X = SCREEN_WIDTH
#Y = SCREEN_HEIGHT

# create the display surface object
# of specific dimension..e(X, Y).
#scrn = pygame.display.set_mode((X, Y))

# set the pygame window name
#pygame.display.set_caption('image')

# create a surface object, image is drawn on it.
#city = pygame.image.load("../assets/background/citybackground.png").convert()
#def Background(fun):
   # blocks = pygame.image.load("../assets/background/blocks.png").convert()
# Using blit to copy content from one surface to other


#draw bottom
# draw the sandy bottom
    #for x in range(0, SCREEN_HEIGHT, TILE_SIZE):
     # fun.blit(blocks, (x, SCREEN_HEIGHT - TILE_SIZE))


#scrn.blit(city, (0, 0))
# paint screen one time
#pygame.display.flip()


#title of game
#custom_font = pygame.font.Font("../assets/fonts/brushed.zip", 48)
#text = custom_font.render("FIGHT",True, (255, 0, 0))
#city.blit(text, (SCREEN_WIDTH / 5, SCREEN_HEIGHT / 10 - text.get_height() / 100))



#while running:
    #for event in pygame.event.get():
      #  if event.type == pygame.QUIT:
        #    running = False

# deactivates the pygame library
#pygame.quit()

