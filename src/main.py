import pygame
from StartScene import StartScene
from config import SCREEN_HEIGHT, SCREEN_WIDTH
from resource import getResource


# Initialize the pygame
pygame.mixer.pre_init(44100, -16, 6, 512)
pygame.init()


# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Title and Icon
pygame.display.set_caption("Trash hunt")
icon = pygame.image.load(getResource("images/icon.png"))
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
