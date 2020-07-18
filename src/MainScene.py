from Scene import Scene
from config import SCREEN_HEIGHT, SCREEN_WIDTH
from Player import Player
import pygame


class MainScene(Scene):
    def __init__(self):
        super().__init__()

        # Player
        self.player = Player((30, (SCREEN_HEIGHT - 64) / 2))
        self.playerGroup = pygame.sprite.RenderPlain(self.player)

        self.accel = 0
        self.ACCEL_CONST = 0.005

    def handleEvent(self, event):
        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.accel -= self.ACCEL_CONST
            if event.key == pygame.K_DOWN:
                self.accel += self.ACCEL_CONST

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.accel = 0

    def render(self, screen):
        self.player.accelerate(self.accel)
        if self.accel == 0:
            self.player.deccelerate()
        self.playerGroup.update()
        # Render Player
        self.playerGroup.draw(screen)
