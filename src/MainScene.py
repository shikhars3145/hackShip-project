from Scene import Scene
import pygame


class MainScene(Scene):
    def __init__(self):
        super().__init__()

        # Player
        self.playerImg = pygame.image.load("src/assets/images/player.png")
        self.playerX = 30
        self.playerY = 268
        self.playerY_Change = 0

    def handleEvent(self, event):
        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.playerY_Change = -0.1
            if event.key == pygame.K_DOWN:
                self.playerY_Change = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.playerY_Change = 0

    def render(self, screen):
        self.playerY += self.playerY_Change
        # Player Boundary
        if self.playerY > 536:
            self.playerY = 536
        if self.playerY < 0:
            self.playerY = 0
        # Render Player
        screen.blit(self.playerImg, (self.playerX, self.playerY))
