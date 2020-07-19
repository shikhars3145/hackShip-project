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

# Average spawn rate of garbage (trash / sec)
GARBAGE_SPAWN_RATE = 2


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

        # Scoring
        self.scoreInt = 0
        self.scoreFont = pygame.font.Font(
            "src/assets/fonts/Lato/Lato-Black.ttf", 32
        )

        # Shark spawn flag.
        self.shouldSpawnSharks = False

        # Shark spawn timer.
        self.spawnSharkAfter = 0

        # Garbage spawn timer.
        self.spawnGarbageAfter = 0

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
                self.player.accelerateUp()
            if event.key == pygame.K_DOWN:
                self.player.accelerateDown()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.player.dampen()

    def render(self, screen):
        currentTime = time_ns()
        delta = (currentTime - self.lastRendered) / 1e9
        self.lastRendered = currentTime

        # Spawn garbage.
        if self.spawnGarbageAfter <= 0:
            self.garbageGroup.add(
                Garbage(
                    (X_UPPER_LIM, random.randint(Y_LOWER_LIM, Y_UPPER_LIM))
                )
            )
            self.spawnGarbageAfter = random.random() / GARBAGE_SPAWN_RATE
        self.spawnGarbageAfter -= delta

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
        self.playerGroup.update(delta)
        self.garbageGroup.update(delta)
        self.sharkGroup.update(delta)

        # Check Collision between garbage and the player
        for garbage in pygame.sprite.groupcollide(
            self.garbageGroup,
            self.playerGroup,
            True,
            False,
            pygame.sprite.collide_mask,
        ):
            self.scoreInt += 1
            self.trashFXbottle.playFX(TRASH_BOTTLE, 0.15)

        # Check shark collision.
        if pygame.sprite.groupcollide(
            self.playerGroup,
            self.sharkGroup,
            True,
            False,
            pygame.sprite.collide_mask,
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
