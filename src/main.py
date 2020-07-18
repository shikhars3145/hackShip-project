import pygame
import os

# Paths
current_path = os.path.dirname(__file__)  # path to main.py

assets_path = os.path.join(current_path, "assets")  # the asssets folder path

images_path = os.path.join(assets_path, "images")  # the images folder path

# Initialize the pygame
pygame.init()


# Create the screen
screen = pygame.display.set_mode((800, 600))


# Title and Icon
pygame.display.set_caption("hackShip project")
icon = pygame.image.load((os.path.join(images_path, "icon.png")))
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load(os.path.join(images_path, "player.png"))
playerX = 30
playerY = 268
playerY_Change = 0

# Function to render Player
def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
RUNNING = True
while RUNNING:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_Change = -0.1
            if event.key == pygame.K_DOWN:
                playerY_Change = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_Change = 0

    playerY += playerY_Change

    # Player Boundary
    if playerY > 536:
        playerY = 536
    if playerY < 0:
        playerY = 0

    # Render Player
    player(playerX, playerY)
    pygame.display.update()
