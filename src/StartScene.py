from Scene import Scene
from MainScene import MainScene
import pygame


class StartScene(Scene):
    def __init__(self):
        super().__init__()
        font = pygame.font.Font("src/assets/fonts/Lato/Lato-Black.ttf", 32)
        self.instruction = font.render(
            "Press Enter to Start ...", True, (255, 255, 255)
        )
        self.shouldStart = False

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            self.shouldStart = True

    def render(self, screen):
        screen.blit(self.instruction, (400, 300))

    def nextScene(self):
        if self.shouldStart:
            return MainScene()
        return self
