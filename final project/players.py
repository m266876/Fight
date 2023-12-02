import pygame
from parameters import *

class Players():
    def __init__(self, x, y, flip, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        #self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 #0:idle 1:run 2:jump 3:attack1 4:attack4 5:hit 6:death
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.running = False
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def load_images(self, sprite_sheet, animation_steps):
    #extract images from spritesheet
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.image_scale * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list

    def move(self, screen_width, screen_height, surface, target):
        speed = SPEED
        gravity = GRAVITY
        dx = 0
        dy = 0
        self.running = False
        self.attack_type = 0


        #keys
        key = pygame.key.get_pressed()


        #can only do other stuff if not currently attacking
        if self.attacking == False:

            #movement
            if key[pygame.K_a]:
                dx = -SPEED
                self.running = True
            if key[pygame.K_d]:
                dx += SPEED
                self.running = True

            #jump
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -30
                self.jump = True
            dy += self.vel_y

            #attack
            if key[pygame.K_r] or key[pygame.K_t]:
                self.attack(surface, target)

                #determine which attack was used
                if key[pygame.K_r]:
                    self.attack_type = 1
                if key[pygame.K_t]:
                    self.attack_type = 2

        #apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #player stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - TILE_SIZE:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - TILE_SIZE - self.rect.bottom

        #ensure players face eachother
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #update player positions
        self.rect.x += dx
        self.rect.y += dy

    #animation updates
    def update(self):
        #check which action the player is performing
        if self.attacking == True:
            if self.attack_type == 1:
                self.update_action(3)
            elif self.attack_type == 2:
                self.update_action(4)
            elif self.jump == True:
                self.update_action(2)
            elif self.running == True:
                self.update_action(1)
            else:
                self.update_action(0)




        animation_cooldown = 50



        #update image
        self.image = self.animation_list[self.action][self.frame_index]
        #check time since last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        #check if the animation has finished
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0


    #attack method
    def attack(self, surface, target):
        self.attacking = True
        attack_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attack_rect.colliderect(target.rect):
            target.health -= 10

        pygame.draw.rect(surface, (0,255,0), attack_rect)

    def update_action(self, new_action):
        #check if new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            #update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()




    def draw(self, surface):
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255,0,0), self.rect)
        surface.blit(img, (self.rect.x, self.rect.y))