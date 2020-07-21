import pygame
from typing import Tuple
from config import X_LOWER_LIM
from KinemeticBody import KinematicBody
from resource import getResource
from animation import splitImage
import random

FRAME_RATE = 10  # per second


class Shark(KinematicBody):
    def __init__(
        self,
        position: Tuple[float, float],
        velocity: Tuple[float, float] = None,
    ):
        original = pygame.image.load(getResource("images/shark.png"))
        self.frames = splitImage(original, 4, 3)[3:6]
        self.currentFrame = 0
        self.timeToNextFrame = 0
        if velocity is None:
            velocity = (random.randint(-250, -200), 0)
        super().__init__(self.frames[0], position, velocity)

    def update(self, delta: float):
        # Animate.
        self.timeToNextFrame -= delta
        if self.timeToNextFrame <= 0:
            self.currentFrame = (self.currentFrame + 1) % len(self.frames)
            self.image = self.frames[self.currentFrame]
            self.timeToNextFrame += 1 / FRAME_RATE

        # Boundary check.
        if self.position[0] < X_LOWER_LIM:
            self.kill()

        super().update(delta)
