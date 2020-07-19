from Scene import Scene
import EndScene
from config import (
    SCREEN_HEIGHT,
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

# Difficulty factors.
INITIAL_SCROLL_SPEED = 100
INITIAL_SHARK_SPAWN_RATE = 0.3
INITIAL_GARBAGE_SPAWN_RATE = 2
SCROLL_SPEED_MULTIPLIER = 0.001
SHARK_SPAWN_RATE_MULTIPLIER = 0.001
GARBAGE_SPAWN_RATE_MULTIPLIER = 0.001
GARBAGE_BONUS_MULTIPLIER = 10
GARBAGE_SPEED_DEVIATION = 50
SHARK_SPEED_DEVIATION = 150


class MainScene(Scene):
    def __init__(self):
        super().__init__()

        # Player
        self.player = Player((30, (SCREEN_HEIGHT - 64) / 2))
        self.playerGroup = pygame.sprite.RenderPlain(self.player)

        # Shark
        self.sharkGroup = pygame.sprite.RenderPlain()

        # Garbage
        self.garbageGroup = pygame.sprite.RenderPlain()

        # Audio
        self.gameMusic = GameAudio(1)
        self.trashFXbottle = GameAudio(2)

        # Difficulty parameters
        # Scrolling speed
        self.scrollSpeed = INITIAL_SCROLL_SPEED
        # Average spawn rate of sharks (sharks / sec)
        self.sharkSpawnRate = INITIAL_SHARK_SPAWN_RATE
        # Average spawn rate of garbage (trash / sec)
        self.garbageSpawnRate = INITIAL_GARBAGE_SPAWN_RATE

        # Performance
        self.garbageCollected = 0
        self.startTime = time_ns()

        # UI
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

    def score(self):
        timeElapsed = int((time_ns() - self.startTime) // 1e9)
        return timeElapsed + self.garbageCollected * GARBAGE_BONUS_MULTIPLIER

    def adjustDifficulty(self):
        """Adjust game difficulty as the score gets higher"""
        score = self.score()
        self.scrollSpeed = (
            INITIAL_SCROLL_SPEED + score * SCROLL_SPEED_MULTIPLIER
        )
        self.sharkSpawnRate = (
            INITIAL_SHARK_SPAWN_RATE + score * SHARK_SPAWN_RATE_MULTIPLIER
        )
        self.garbageSpawnRate = (
            INITIAL_GARBAGE_SPAWN_RATE + score * GARBAGE_SPAWN_RATE_MULTIPLIER
        )

    def handleEvent(self, event):
        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player.acceleration = (
                    self.player.acceleration[0],
                    -self.player.ACCEL_CONST,
                )
            elif event.key == pygame.K_DOWN:
                self.player.acceleration = (
                    self.player.acceleration[0],
                    self.player.ACCEL_CONST,
                )
            elif event.key == pygame.K_LEFT:
                self.player.acceleration = (
                    -self.player.ACCEL_CONST,
                    self.player.acceleration[1],
                )
            elif event.key == pygame.K_RIGHT:
                self.player.acceleration = (
                    self.player.ACCEL_CONST,
                    self.player.acceleration[1],
                )

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.player.acceleration = (self.player.acceleration[0], 0)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.player.acceleration = (0, self.player.acceleration[1])

    def render(self, screen):
        currentTime = time_ns()
        delta = (currentTime - self.lastRendered) / 1e9
        self.lastRendered = currentTime

        # Adjust difficulty.
        self.adjustDifficulty()

        # Spawn garbage.
        if self.spawnGarbageAfter <= 0:
            self.garbageGroup.add(
                Garbage(
                    (X_UPPER_LIM, random.randint(Y_LOWER_LIM, Y_UPPER_LIM)),
                    (
                        -self.scrollSpeed
                        - random.random() * GARBAGE_SPEED_DEVIATION,
                        0,
                    ),
                )
            )
            self.spawnGarbageAfter = random.random() / self.garbageSpawnRate
        self.spawnGarbageAfter -= delta

        # Start spawning sharks after peaceful theme ends.
        if not self.gameMusic.is_busy():
            self.shouldSpawnSharks = True
            self.gameMusic.playLooped(DANGER_LOOP, 0.3)

        if self.shouldSpawnSharks:
            if self.spawnSharkAfter <= 0:
                self.sharkGroup.add(
                    Shark(
                        (
                            X_UPPER_LIM,
                            random.randint(Y_LOWER_LIM, Y_UPPER_LIM),
                        ),
                        (
                            -self.scrollSpeed
                            - random.random() * SHARK_SPEED_DEVIATION,
                            0,
                        ),
                    )
                )
                self.spawnSharkAfter = random.random() / self.sharkSpawnRate
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
            self.garbageCollected += 1
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
            self.scoreFont.render(str(self.score()), True, (255, 255, 255)),
            (20, 20),
        )

    def nextScene(self):
        if self.gameOver:
            self.gameMusic.stop()
            return EndScene.EndScene(self.score())
        return self
