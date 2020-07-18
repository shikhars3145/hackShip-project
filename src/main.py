import pygame

# Initialize the pygame
pygame.init()


# Create the screen
screen = pygame.display.set_mode((800, 600))


# Title and Icon
pygame.display.set_caption('hackShip project')
# icon = pygame.image.load('./scuba-diver.png')
# pygame.display.set_icon(icon)


# Game Loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    pygame.display.update()
