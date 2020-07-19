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
from time import time_ns
import pygame
import random

PEACEFUL_LOOP = "src/assets/audio/bgmLoop.wav"
PEACEFUL_LOOP_COUNT = 1
DANGER_LOOP = "src/assets/audio/bgmLoopShark.wav"
TRASH_BOTTLE = "src/assets/audio/trashBottle.wav"

# Average spawn rate of sharks (sharks / sec)
SHARK_SPAWN_RATE = 0.3


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

        # Shark spawn flag.
        self.shouldSpawnSharks = False

        # Shark spawn timer.
        self.spawnSharkAfter = 0

        # Game over flag.
        self.gameOver = False

        # Audio
        self.gameMusic.playLooped(PEACEFUL_LOOP, 0.3, PEACEFUL_LOOP_COUNT)

        # Timestamp of the last render.
        self.lastRendered = time_ns()

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
        currentTime = time_ns()
        delta = (currentTime - self.lastRendered) / 1e9
        self.lastRendered = currentTime

        # Start spawning sharks after peaceful theme ends.
        if not self.gameMusic.is_busy():
            self.shouldSpawnSharks = True
            self.gameMusic.playLooped(DANGER_LOOP, 0.3)

        if self.shouldSpawnSharks:
            if self.spawnSharkAfter <= 0:
                self.sharkGroup.add(
                    Shark(
                        (X_UPPER_LIM, random.randint(Y_LOWER_LIM, Y_UPPER_LIM))
                    )
                )
                self.spawnSharkAfter = random.random() / SHARK_SPAWN_RATE
            self.spawnSharkAfter -= delta
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
