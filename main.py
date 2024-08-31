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

clock = pygame.time.Clock()


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


def main():
    # player Y = up/down
    PLAYER_Y = 500

    # player X = right left
    PLAYER_X = 600

    # player scale aka Z coordinate
    PLAYER_Z = 3

    # x coordinate walk speed
    X_speed = 8

    # y coordinate walk speed
    Y_speed = 2
    # initialize character sprite sheet
    char_images = []

    # set run game to True
    run = True

    #set character sprite sheet as emily_sheet (will be a selectable variable later
    character_sheet = emily_sheet

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
                    PLAYER_X -= X_speed
                    facing = 3
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1
                """Right direction from arrow or 'd' key"""
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    PLAYER_X += X_speed
                    facing = 1
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1
                """Up direction from arrow or 'w' key"""
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if HEIGHT - PLAYER_Y < 900:
                        PLAYER_Y -= Y_speed
                    if X_speed > 5:
                        X_speed -= 2
                    if Y_speed > 1:
                        Y_speed -= 1
                    if PLAYER_Z >= 2:
                        PLAYER_Z -= .5
                    facing = 2
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1
                """Down direction from arrow or 's' key"""
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if HEIGHT - PLAYER_Y > 100:
                        PLAYER_Y += Y_speed
                    X_speed += 2
                    if Y_speed > 1:
                        Y_speed -= 1

                    PLAYER_Z += .5
                    facing = 0
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1
                """Flying direction from space bar and up arrow"""
                if event.key == pygame.K_SPACE and pygame.K_UP:  # not working properly yet
                    character_sheet = flying_sheet
                    if HEIGHT - PLAYER_Y < 900:
                        PLAYER_Y -= 6
                    if counter == 3:
                        counter = 0
                    else:
                        counter += 1
                """Draw player to screen using created variables"""
                print(PLAYER_Y, "y coord")
                print(PLAYER_X, "x coord")
                image = get_image(character_sheet, facing, counter, 16, 32, PLAYER_Z, BLACK)
                player = Character(image, PLAYER_X, PLAYER_Y)
                draw(player)
                pygame.display.update()
            else:
                """Draw player using default variables when no keys are pushed"""
                image = get_image(character_sheet, facing, 0, 16, 32, PLAYER_Z, BLACK)
                player = Character(image, PLAYER_X, PLAYER_Y)
                draw(player)
                pygame.display.update()



    pygame.quit()


if __name__ == "__main__":

    main()