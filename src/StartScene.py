from Scene import Scene
from MainScene import MainScene
import pygame
from GameAudio import GameAudio
from Rail import ForegroundRail, MiddlegroundRail, BackgroundRail
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from time import time_ns

PARALLAX_RATIO = 0.5


class StartScene(Scene):
    def __init__(self):
        super().__init__()
        font = pygame.font.Font("src/assets/fonts/Lato/Lato-Black.ttf", 32)
        titleFont = pygame.font.Font(
            "src/assets/fonts/Lato/Lato-Black.ttf", 64
        )
        self.title = titleFont.render("Trash Hunt", True, (255, 255, 255))
        self.instruction = font.render(
            "Press Enter to Start", True, (255, 255, 255)
        )
        self.shouldStart = False

        # Audio
        self.gameMusic = GameAudio(0)
        self.gameMusic.playLooped("src/assets/audio/bgmLoopIntro.wav", 0.3)

        # Background
        self.scrollSpeed = 300
        self.lastUpdated = time_ns()
        self.foreground = ForegroundRail((0, 410), -600, -self.scrollSpeed)
        self.middleground = MiddlegroundRail(
            (0, 200), -600, -self.scrollSpeed * PARALLAX_RATIO
        )
        self.background = BackgroundRail(
            (0, 0), -1024, -self.scrollSpeed * PARALLAX_RATIO ** 2
        )

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            self.shouldStart = True

    def render(self, screen):
        currentTime = time_ns()
        delta = (currentTime - self.lastUpdated) / 1e9
        self.lastUpdated = currentTime
        self.background.update(delta)
        self.middleground.update(delta)
        self.foreground.update(delta)
        self.background.draw(screen)
        self.middleground.draw(screen)
        self.foreground.draw(screen)
        screen.blit(
            self.title,
            self.title.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100)),
        )
        screen.blit(
            self.instruction,
            self.instruction.get_rect(
                center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            ),
        )

    def nextScene(self):
        if self.shouldStart:
            self.gameMusic.stop()
            return MainScene()
        return self
