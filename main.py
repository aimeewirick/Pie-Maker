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
    # player Y = up/down
    PLAYER_Y = 500

    # player X = right left
    PLAYER_X = 600

    # set run game to True
    run = True

    # track sprite image iteration
    counter = 0
    # initialize character image variable
    image = None
    # initialize character facing
    facing = 0   # 0=forward 1=right 2=back 3=left

    pygame.key.set_repeat(1, 100)

    while run:
        """Checking for in-game events"""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                """allow player to exit game"""
                run = False
                break
            """Checking for player keyboard input"""
            if event.type == pygame.KEYDOWN:

                """Left direction from arrow or 'a' key"""
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    PLAYER_X -= 6
                    facing = 3
                    image = l_images[counter]
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1
                """Right direction from arrow or 'd' key"""
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    PLAYER_X += 6
                    facing = 1
                    image = r_images[counter]
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1
                """Up direction from arrow or 'w' key"""
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if HEIGHT - PLAYER_Y < 900:
                        PLAYER_Y -= 6
                    facing = 2
                    image = u_images[counter]
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1
                """Down direction from arrow or 's' key"""
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if HEIGHT - PLAYER_Y > 100:
                        PLAYER_Y += 6
                    facing = 0
                    image = d_images[counter]
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1
                """Flying direction from space bar and up arrow"""
                if event.key == pygame.K_SPACE and pygame.K_UP:  # not working properly yet
                    if HEIGHT - PLAYER_Y < 900:
                        PLAYER_Y -= 6
                    image = flying_images[counter]
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1
                """Draw player to screen using created variables"""
                player = Character(image, PLAYER_X, PLAYER_Y)
                draw(player)
                pygame.display.update()
            else:
                """Draw player using default variables when no keys are pushed"""
                image = get_image(emily_sheet, facing, 0, 16, 32, 3, BLACK)
                player = Character(image, PLAYER_X, PLAYER_Y)
                draw(player)
                pygame.display.update()



    pygame.quit()


if __name__ == "__main__":

    main()