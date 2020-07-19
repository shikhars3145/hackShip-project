import pygame
from typing import Tuple
from config import X_LOWER_LIM
from KinemeticBody import KinematicBody
import random


class Shark(KinematicBody):
    def __init__(
        self,
        position: Tuple[float, float],
        velocity: Tuple[float, float] = None,
    ):
        image = pygame.image.load("src/assets/images/shark.png")
        image = pygame.transform.scale(image, (128, 64))
        if velocity is None:
            velocity = (random.randint(-250, -200), 0)
        super().__init__(image, position, velocity)

    def update(self, delta: float):
        super().update(delta)

        # Boundary check.
        if self.position[0] < X_LOWER_LIM:
            self.kill()
