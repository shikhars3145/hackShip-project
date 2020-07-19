import pygame
import math
from typing import Tuple
from time import time_ns


# Player sprite.
class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        position: Tuple[float, float],
        velocity: Tuple[float, float] = (0, 0),
    ):
        super().__init__()
        self.image = pygame.image.load("src/assets/images/player.png")
        self.position = position
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = velocity
        self.DECCEL_VAL = 6
        self.ACCEL_CONST = 7
        self.accel = 0
        self.lastUpdated = time_ns()

    def update(self):
        delta = (time_ns() - self.lastUpdated) / 1e9
        self.lastUpdated = time_ns()
        if self.accel == 0:
            # Damping.
            self.position = (
                self.position[0],
                self.position[1]
                + (1 - math.exp(-self.DECCEL_VAL * delta)) / self.DECCEL_VAL
                + self.velocity[1] * delta,
            )
            self.velocity = (
                self.velocity[0],
                self.velocity[1] * (1 - self.DECCEL_VAL * delta),
            )
        else:
            # Accelerate.
            self.position = (
                self.position[0],
                self.position[1]
                + self.velocity[1] * delta
                + self.accel * delta * delta / 2,
            )
            self.velocity = (self.velocity[0], self.velocity[1] + self.accel)
        # Update rect.
        self.rect = self.image.get_rect(center=self.position)
