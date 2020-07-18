import pygame
from StartScene import StartScene
from config import SCREEN_HEIGHT, SCREEN_WIDTH

# Initialize the pygame
pygame.init()


# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Title and Icon
pygame.display.set_caption("hackShip project")
icon = pygame.image.load("src/assets/images/icon.png")
pygame.display.set_icon(icon)

# Scene
scene = StartScene()

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
    scene = scene.nextScene()
