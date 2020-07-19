import pygame
from typing import Tuple
from KinemeticBody import KinematicBody


# Player sprite.
class Player(KinematicBody):
    def __init__(
        self, position: Tuple[float, float],
    ):
        super().__init__(
            pygame.image.load("src/assets/images/player.png"), position,
        )
        self.DECCEL_VAL = 3
        self.ACCEL_CONST = 2500
        self.isDamping = False

    def accelerateUp(self):
        self.isDamping = False
        self.acceleration = (0, -self.ACCEL_CONST)

    def accelerateDown(self):
        self.isDamping = False
        self.acceleration = (0, self.ACCEL_CONST)

    def dampen(self):
        self.isDamping = True

    def update(self, delta: float):
        if self.isDamping:
            self.acceleration = (
                -self.velocity[0] * self.DECCEL_VAL,
                -self.velocity[1] * self.DECCEL_VAL,
            )
        super().update(delta)
