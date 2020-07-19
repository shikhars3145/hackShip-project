from Scene import Scene
from MainScene import MainScene
import pygame
from GameAudio import GameAudio


class StartScene(Scene):
    def __init__(self):
        super().__init__()
        font = pygame.font.Font("src/assets/fonts/Lato/Lato-Black.ttf", 32)
        self.instruction = font.render(
            "Press Enter to Start ...", True, (255, 255, 255)
        )
        self.shouldStart = False

        # Audio
        self.gameMusic = GameAudio(0)
        self.gameMusic.playLooped("src/assets/audio/bgmLoopIntro.wav", 0.3)

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            self.shouldStart = True

    def render(self, screen):
        screen.blit(self.instruction, (400, 300))

    def nextScene(self):
        if self.shouldStart:
            self.gameMusic.stop()
            return MainScene()
        return self
