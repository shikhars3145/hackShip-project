from Scene import Scene
from resource import getResource
import MainScene
import pygame


class EndScene(Scene):
    def __init__(self, score: int):
        super().__init__()

        font = pygame.font.Font(getResource("fonts/Lato/Lato-Black.ttf"), 32)
        self.title = font.render(
            "Game Over", True, (255, 0, 0)
        )
        self.scoreMessage = font.render(
            f"Your score is : {score}", True, (255, 255, 255)
        )
        self.instruction = font.render(
            "Press 'R' key to restart.", True, (255, 255, 255)
        )
        self.shouldStart = False

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                self.shouldStart = True

    def render(self, screen):
        screen.blit(self.title, (200, 100))
        screen.blit(self.scoreMessage, (200, 200))
        screen.blit(self.instruction, (200, 300))

    def nextScene(self):
        if self.shouldStart:
            return MainScene.MainScene()
        return self
