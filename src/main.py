import pygame
import os
from MainScene import MainScene

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

# Scene
scene = MainScene()

# Game Loop
RUNNING = True
while RUNNING:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        scene.handleEvent(event)

    scene.render(screen)
    pygame.display.update()
