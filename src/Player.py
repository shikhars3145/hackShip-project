import pygame
from typing import Tuple
from KinemeticBody import KinematicBody
from config import SCREEN_HEIGHT, SCREEN_WIDTH
from resource import getResource
from animation import splitImage


FRAME_RATE = 10
PLAYER_SPRITE_SHEET = pygame.image.load(
    getResource("images/underwater-diving/player/player-swimming.png")
)


# Player sprite.
class Player(KinematicBody):
    def __init__(
        self, position: Tuple[float, float],
    ):
        self.frames = splitImage(PLAYER_SPRITE_SHEET, 1, 7)
        self.currentFrame = 0
        self.timeToNextFrame = 0
        super().__init__(self.frames[0], position)
        self.damping_constant = 1
        self.ACCEL_CONST = 2500

    def update(self, delta: float):
        # Animate.
        self.timeToNextFrame -= delta
        if self.timeToNextFrame <= 0:
            self.currentFrame = (self.currentFrame + 1) % len(self.frames)
            self.image = self.frames[self.currentFrame]
            self.timeToNextFrame += 1 / FRAME_RATE

        # Player Boundary
        if self.position[0] < 32:
            self.velocity = (0, self.velocity[1])
            self.position = (32, self.position[1])

        if self.position[0] > SCREEN_WIDTH - 32:
            self.velocity = (0, self.velocity[1])
            self.position = (SCREEN_WIDTH - 32, self.position[1])

        if self.position[1] < 32:
            self.velocity = (self.velocity[0], 0)
            self.position = (self.position[0], 32)

        if self.position[1] > SCREEN_HEIGHT - 32:
            self.velocity = (self.velocity[0], 0)
            self.position = (self.position[0], SCREEN_HEIGHT - 32)

        super().update(delta)
