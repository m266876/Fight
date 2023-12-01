import pygame
import sys
import random
from parameters import *
from background import *
import button
from bullets import *
from gunman import *
from zombie import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("FIGHT")
clock = pygame.time.Clock()

scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('PLAY')

#HOME SCREEN
#button images
play_btn = pygame.image.load('../final project/sprites/1.png').convert_alpha()
exit_img = pygame.image.load('../final project/sprites/16.png').convert_alpha()
menu_img = pygame.image.load('../final project/background/homescreen.png').convert_alpha()

#button instances
play_button = button.Button(100, 50, play_btn, .5)
exit_button = button.Button(800, 100, exit_img, .5)

#loop
run_home_screen = True

while run_home_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_home_screen = False

    scrn.blit(menu_img, (0, 0))
    if play_button.draw(scrn):
        run_home_screen = False

    if exit_button.draw(scrn):
        pygame.quit()
        sys.exit()

    custom_font = pygame.font.Font("../final project/fonts/Black_Crayon.ttf", 48)
    text = custom_font.render("FIGHT", True, (255, 0, 0))
    scrn.blit(text, (SCREEN_WIDTH / 5, SCREEN_HEIGHT / 10 - text.get_height() / 2))

    pygame.display.flip()
    clock.tick(60)

background = scrn.copy()
draw_background(background)

# Game loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#loading bar

def main():
    bar_width = 0
    start_time = pygame.time.get_ticks()
    duration = 5000  # 5 seconds in milliseconds

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Calculate the elapsed time
        elapsed_time = pygame.time.get_ticks() - start_time

        # Update the bar width based on elapsed time
        if elapsed_time < duration:
            bar_width = int((elapsed_time / duration) * BAR_WIDTH)
        else:
            bar_width = BAR_WIDTH

        # Clear the screen
        scrn.fill(background)

        # Draw the bar
        pygame.draw.rect(scrn, BAR_COLOR, (WIDTH // 2 - BAR_WIDTH // 2, HEIGHT // 2 - BAR_HEIGHT // 2, bar_width, BAR_HEIGHT))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

        # Check if the duration has passed, and exit the loop
        if elapsed_time >= duration + 1000:  # Add an extra second before exiting
            break


LIVES1 = 3
LIVES2 = 3



#players
while lives1 > 0 and lives2 > 0 and running:
    class gunman(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(sprite_sheet_image, (50, 38))
            self.image.set_colorkey((0, 0))
            self.rect = self.image.get_rect()
            self.rect.centerx = SCREEN_WIDTH / 2
            self.rect.bottom = SCREEN_HEIGHT - 10
            self.speedx = 0
            self.speedy = 0
            self.is_jumping = False
            self.lives1 = 3  # Initial number of lives
            self.hitbox = pygame.Rect(0,0,30,30)
            self.hitbox.center = self.rect.center


        def update(self):
            if self.lives1 > 0:  # Check if lives are greater than 0
                self.speedx = 0
                keystate = pygame.key.get_pressed()

                if keystate[pygame.K_a]:
                    self.speedx = -5
                if keystate[pygame.K_d]:
                    self.speedx = 5

                if not self.is_jumping and keystate[pygame.K_w]:
                    self.is_jumping = True
                    self.speedy = -5

                if self.is_jumping:
                    self.rect.y += self.speedy
                    self.speedy += 0.2

                    if self.rect.bottom >= SCREEN_HEIGHT - TILE_SIZE:
                        self.rect.bottom = SCREEN_HEIGHT - TILE_SIZE
                        self.is_jumping = False
                        self.speedy = 0

                self.rect.x += self.speedx

                if self.rect.right > SCREEN_WIDTH:
                    self.rect.right = SCREEN_WIDTH
                if self.rect.left < 0:
                    self.rect.left = 0
            else:
            # Game over logic or other actions when lives are 0
                pass
            self.hitbox.center = self.rect.center

        def create_bullet(self):
            return Bullet(gunman.rect.center()[0], pygame.mouse.get_pos()[1])



        class zombie(pygame.sprite.Sprite):
            def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.transform.scale(sprite_sheet_image, (50, 38))
                self.image.set_colorkey((0, 0))
                self.rect = self.image.get_rect()
                self.rect.centerx = SCREEN_WIDTH / 2
                self.rect.bottom = SCREEN_HEIGHT - 10
                self.speedx = 0
                self.speedy = 0
                self.is_jumping = False
                self.lives2 = 3  # Initial number of lives
                self.hitbox = pygame.Rect(0,0,30,30)
                self.hitbox.center = self.rect.center

            def update(self):
                if self.lives2 > 0:  # Check if lives are greater than 0
                    self.speedx = 0
                    keystate = pygame.key.get_pressed()

                    if keystate[pygame.K_LEFT]:
                        self.speedx = -5
                    if keystate[pygame.K_RIGHT]:
                        self.speedx = 5

                    if not self.is_jumping and keystate[pygame.K_UP]:
                        self.is_jumping = True
                        self.speedy = -5

                    if self.is_jumping:
                        self.rect.y += self.speedy
                        self.speedy += 0.2

                        if self.rect.bottom >= SCREEN_HEIGHT - TILE_SIZE:
                            self.rect.bottom = SCREEN_HEIGHT - TILE_SIZE
                            self.is_jumping = False
                            self.speedy = 0

                    self.rect.x += self.speedx

                    if self.rect.right > SCREEN_WIDTH:
                        self.rect.right = SCREEN_WIDTH
                    if self.rect.left < 0:
                        self.rect.left = 0
                else:
                # Game over logic or other actions when lives are 0
                    pass
                self.hitbox.center = self.rect.center

            def create_bullet(self):
                return Bullet(zombie.rect.center()[0], pygame.mouse.get_pos()[1])

    platforms.update()
    gunman.update()
    zombie.update()


#score
#more bullet stuff

bullet_group = pygame.sprite.Group()
bullet_ready = False
bullet_group = []

#loopity loop loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_F:
            bullet_group.add(gunman.create_bullet())
        if event.type == pygame.K_CTRL:
            bullet_group.add(zombie.create_bullet())

    sprites.update()

    scrn.fill(city)
    sprites.draw(scrn)
    bullet_group.draw(scrn)
    pygame.display.flip()


#game over
scrn.blit(background, (0, 0))
font = pygame.font.Font("../final project/fonts/Brainfish_Rush.ttf")
#show game over message
message = font.render("GAME OVER", True, (0, 0, 0))
scrn.blit(message, (SCREEN_WIDTH / 2 - message.get_width() /2, SCREEN_HEIGHT /2))

#show final score
score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
scrn.blit(score_text, (SCREEN_WIDTH /2 - score_text.get_width() /2, SCREEN_HEIGHT / 2 + score_text.get_height()))

#MUSAK
pygame.mixer.music.load('../final project/sound/Runaway.mp3')

# Set the volume (optional)
pygame.mixer.music.set_volume(0.5)

# Play the music indefinitely
pygame.mixer.music.play(-1)



pygame.quit()