import pygame
from typing import Tuple
from KinemeticBody import KinematicBody
from config import SCREEN_HEIGHT, SCREEN_WIDTH


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
