import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


# import sprite sheet
sprite_sheet_image = pygame.image.load('zombierun.png').convert()

# clock object
clock = pygame.time.Clock()

RGB = (10, 150, 150)
color = (247, 247, 247)


# get images
def get_image(sheet, frame_x, frame_y, width, height, scale, color):
    image = pygame.Surface((width, height)).convert()
    image.set_colorkey((color))
    image.blit(sheet, (0, 0), (frame_x * width, frame_y * height, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image


# loop through sprite sheet to get images
all_frames = []
idx = 0

for x in range(5):
    for y in range(2):
        all_frames.insert(idx, get_image(sprite_sheet_image, x, y, 172, 183, .5, color))
        idx += 1

run = True

while run:

    # update background
    screen.fill(RGB)

    # show frame image
    for x in range(len(all_frames)):
        screen.blit(all_frames[x], (x * 75, 0))

        #uncomment these if you want to see the figure moving on the screen
        screen.fill(RGB)
        screen.blit(all_frames[x], (75, 0))
        pygame.display.flip()
        clock.tick(30)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

#if zombie hit gunny
hits = pygame.sprite.spritecollide(zombie, gunman, False)
if hits:
    run = False


    pygame.display.flip()

pygame.quit()