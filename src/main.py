import pygame
import os

# Paths
current_path = os.path.dirname(__file__)  # path to main.py

assets_path = os.path.join(current_path, 'assets')  # the asssets folder path

images_path = os.path.join(assets_path, 'images')  # the images folder path

# Initialize the pygame
pygame.init()


# Create the screen
screen = pygame.display.set_mode((800, 600))


# Title and Icon
pygame.display.set_caption('hackShip project')
icon = pygame.image.load((os.path.join(images_path, 'icon.png')))
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load(os.path.join(images_path, 'player.png'))
playerX = 30
playerY = 268


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    player(playerX, playerY)
    pygame.display.update()
