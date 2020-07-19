from Scene import Scene
import EndScene
from config import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    X_UPPER_LIM,
    Y_LOWER_LIM,
    Y_UPPER_LIM,
)
from Player import Player
from Shark import Shark
from Garbage import Garbage
from GameAudio import GameAudio
import pygame
import random

BMG_LOOP = "src/assets/audio/bgmLoop.wav"
TRASH_BOTTLE = "src/assets/audio/trashBottle.wav"


class MainScene(Scene):
    gameMusic = GameAudio(1)
    trashFXbottle = GameAudio(2)

    def __init__(self):
        super().__init__()

        # Player
        self.player = Player((30, (SCREEN_HEIGHT - 64) / 2))
        self.playerGroup = pygame.sprite.RenderPlain(self.player)

        # Shark
        self.sharkGroup = pygame.sprite.RenderPlain()
        self.sharkGroup.add(
            Shark((X_UPPER_LIM, random.randint(Y_LOWER_LIM, Y_UPPER_LIM)))
        )

        # Garbage
        self.garbageGroup = pygame.sprite.RenderPlain()
        for i in range(5):
            self.garbage = Garbage(
                (
                    random.randint(SCREEN_WIDTH // 4, X_UPPER_LIM),
                    random.randint(Y_LOWER_LIM, Y_UPPER_LIM),
                )
            )
            self.garbageGroup.add(self.garbage)

        # Scoring
        self.scoreInt = 0
        self.scoreFont = pygame.font.Font(
            "src/assets/fonts/Lato/Lato-Black.ttf", 32
        )

        # Game over flag.
        self.gameOver = False

        # Audio
        self.gameMusic.playLooped(BMG_LOOP, 0.3)

    def handleEvent(self, event):
        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player.accel -= self.player.ACCEL_CONST
            if event.key == pygame.K_DOWN:
                self.player.accel += self.player.ACCEL_CONST

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.player.accel = 0

    def render(self, screen):
        # Update
        self.playerGroup.update()
        self.garbageGroup.update()
        self.sharkGroup.update()

        # Check Collision between garbage and the player
        for garbageInstance in self.garbageGroup:
            if pygame.sprite.collide_mask(self.player, garbageInstance):
                self.scoreInt += 1
                self.trashFXbottle.playFX(TRASH_BOTTLE, 0.15)
                garbageInstance.reset()

        # Check shark collision.
        if pygame.sprite.groupcollide(
            self.playerGroup, self.sharkGroup, True, False
        ):
            # Shark collision detected.
            # Game over.
            self.gameOver = True

        # Render Player
        self.playerGroup.draw(screen)
        self.garbageGroup.draw(screen)
        self.sharkGroup.draw(screen)
        # Render score
        screen.blit(
            self.scoreFont.render(str(self.scoreInt), True, (255, 255, 255)),
            (20, 20),
        )

    def nextScene(self):
        if self.gameOver:
            self.gameMusic.stop()
            return EndScene.EndScene(self.scoreInt)
        return self
