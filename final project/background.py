import pygame
from parameters import *

# Activate the pygame library.
pygame.init()

X = SCREEN_WIDTH
Y = SCREEN_HEIGHT

# Create the display surface object of specific dimensions (X, Y).
scrn = pygame.display.set_mode((X, Y))
pygame.display.set_caption('image')

city = pygame.image.load("../final project/background/citybackground.png").convert()
blocks = pygame.surface.Surface("../final project/background/blocks.png").convert()

def draw_background(surface):
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        surface.blit(blocks, (x, SCREEN_HEIGHT - TILE_SIZE))

#platforms
# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()

# Variable to store the
# velocity of the platform
platform_vel = 5

# Starting coordinates of the platform
x = 100
y = 150


# Creating a rect with width
# and height
rect = blocks(x, y, 200, 50)

# Creating a boolean variable that
# we will use to run the while loop
run = True

# Creating an infinite loop
# to run our game
while run:

    # Setting the frame rate to 30fps
    clock.tick(30)

    # Multiplying platform_vel with -1
    # if its x coordinate is less than 100
    # or greater than or equal to 300.
    if rect.left >= 300 or rect.left < 100:
        platform_vel *= -1

    # Adding platform_vel to x
    # coordinate of our rect
    rect.left += platform_vel

    # Drawing the rect on the screen using the
    # draw.rect() method
    pygame.draw.rect(scrn, (255, 0, 0), rect)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background
    draw_background(scrn)

    # Draw the city background
    scrn.blit(city, (0, 0))

    # Draw the text
    custom_font = pygame.font.Font("../../chomp/assets/fonts/brushed.zip", 48)
    text = custom_font.render("FIGHT", True, (255, 0, 0))
    scrn.blit(text, (SCREEN_WIDTH / 5, SCREEN_HEIGHT / 10 - text.get_height() / 2))

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

