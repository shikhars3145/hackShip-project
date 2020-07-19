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
        self.damping_constant = 1
        self.ACCEL_CONST = 2500

    def update(self, delta: float):
        super().update(delta)
