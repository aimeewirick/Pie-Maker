import pygame
import time
import random
from pygame.locals import*
from PIL import Image
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
emily_sheet = pygame.image.load('Emily.png').convert_alpha()
flying_sheet = pygame.image.load('Emily_fairy.png').convert_alpha()

BLACK = (0, 0, 0)
global PLAYER_X
global PLAYER_Y
l_images = []
r_images = []
u_images = []
d_images = []
flying_images = []
clock = pygame.time.Clock()

def get_image(sheet, line, frame, width, height, scale, color):
    image = pygame.Surface((width, height)).convert_alpha()
    image.blit(sheet, (0, 0), ((frame * width), line * height, width, height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    image.set_colorkey(color)
    return image


for x in range(4): #settinp up facing sprite sheets
    l_images.append(get_image(emily_sheet, 3, x, 16, 32, 3, BLACK))
    r_images.append(get_image(emily_sheet, 1, x, 16, 32, 3, BLACK))
    u_images.append(get_image(emily_sheet, 2, x, 16, 32, 3, BLACK))
    d_images.append(get_image(emily_sheet, 0, x, 16, 32, 3, BLACK))


for x in range(4):
    flying_images.append(get_image(flying_sheet, 0, x, 28, 35, 3, BLACK))

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


def main():

    PLAYER_Y = 500
    PLAYER_X = 600
    run = True
    iteration = 0
    counter = 0
    image = None
    facing = 0
    event_list = [K_LEFT, K_RIGHT, K_UP, K_DOWN, K_a, K_d, K_w, K_s]
    pygame.key.set_repeat(1, 100)

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    PLAYER_X -= 6
                    facing = 3
                    image = l_images[counter]
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1

                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    PLAYER_X += 6
                    facing = 1
                    image = r_images[counter]
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1

                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if HEIGHT - PLAYER_Y < 900:
                        PLAYER_Y -= 6
                    facing = 2
                    image = u_images[counter]
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1

                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if HEIGHT - PLAYER_Y > 100:
                        PLAYER_Y += 6
                    facing = 0
                    image = d_images[counter]
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1

                if event.key == pygame.K_SPACE:
                    if HEIGHT - PLAYER_Y < 900:
                        PLAYER_Y -= 6
                    image = flying_images[counter]
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1

                player = Character(image, PLAYER_X, PLAYER_Y)
                draw(player)
                pygame.display.update()
            else:
                image = get_image(emily_sheet, facing, 0, 16, 32, 3, BLACK)
                player = Character(image, PLAYER_X, PLAYER_Y)
                draw(player)
                pygame.display.update()



    pygame.quit()


if __name__ == "__main__":

    main()