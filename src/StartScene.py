from Scene import Scene
from MainScene import MainScene
import pygame
from GameAudio import GameAudio
import time

class StartScene(Scene):
    gameMusic = GameAudio(0)
    def __init__(self):
        super().__init__()
        font = pygame.font.Font("src/assets/fonts/Lato/Lato-Black.ttf", 32)
        self.instruction = font.render(
            "Press Enter to Start ...", True, (255, 255, 255)
        )
        self.shouldStart = False

        #self.gameMusic.playLooped('src/assets/audio/bgmLoopIntro.wav', 0.7)


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

    def checkCollision(self):
        pass
