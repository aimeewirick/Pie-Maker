import pygame
import time
import random
from pygame.locals import*
from PIL import Image

pygame.init()
WIDTH, HEIGHT = 1800, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Berry Picker")
BG = pygame.image.load("Trees_field.jpg").convert()
grass_walk = pygame.mixer.Sound('Footsteps_grass_wind.wav')#this doesn't sound right
BLACK = (0, 0, 0)
global PLAYER_X
global PLAYER_Y

def get_image(sheet, line, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), line * height, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image


class Character:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    def draw_char(self, screen):
        WIN.blit(self.image, (self.x, self.y))


def draw(player):

    WIN.blit(BG, (0, 0))
    player.draw_char(WIN)
    pygame.display.update()


def animate_char(sprite_sheet, facing, PLAYER_X, PLAYER_Y, last_update, frame):
    sequence = 4
    animation_cooldown = 0
    animation_list = []
    for x in range(sequence):
        animation_list.append(get_image(sprite_sheet, facing, x, 16, 32, 3, BLACK))
    current_time = pygame.time.get_ticks()

    if current_time - last_update >= animation_cooldown:
        if frame == 4:
            frame = 0
        frame += 1
        player = Character(animation_list[frame], PLAYER_X, PLAYER_Y)
        draw(player)
        pygame.display.update()
    last_update = current_time
    return last_update, frame


def main():
    PLAYER_Y = 500
    PLAYER_X = 600
    run = True
    last_update = pygame.time.get_ticks()
    sprite_sheet = pygame.image.load('Emily.png').convert_alpha()
    player = None
    facing = 0
    frame = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            PLAYER_X -= 1
            facing = 3
            animate_char(sprite_sheet, facing, PLAYER_X, PLAYER_Y, last_update, frame)

        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            PLAYER_X += 1
            facing = 1
            animate_char(sprite_sheet, facing, PLAYER_X, PLAYER_Y, last_update, frame)

        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if HEIGHT - PLAYER_Y < 900:
                PLAYER_Y -= 1
            facing = 2
            animate_char(sprite_sheet, facing, PLAYER_X, PLAYER_Y, last_update, frame)

        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if HEIGHT - PLAYER_Y > 100:
                PLAYER_Y += 1
            facing = 0
            animate_char(sprite_sheet, facing, PLAYER_X, PLAYER_Y, last_update, frame)

        else:
            frame = 0
            image = get_image(sprite_sheet, facing, 0, 16, 32, 3, BLACK)
            player = Character(image, PLAYER_X, PLAYER_Y)
            draw(player)
            pygame.display.update()

    pygame.quit()


if __name__ == "__main__":

    main()

