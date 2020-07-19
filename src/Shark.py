import pygame
from typing import Tuple
from time import time_ns
from config import X_LOWER_LIM, X_UPPER_LIM, Y_LOWER_LIM, Y_UPPER_LIM
import random


class Shark(pygame.sprite.Sprite):
    def __init__(
        self,
        position: Tuple[float, float],
        velocity: Tuple[float, float] = (random.randint(-250, -200), 0),
    ):
        super().__init__()
        self.image = pygame.image.load("src/assets/images/shark.png")
        self.image = pygame.transform.scale(self.image, (128, 64))
        self.position = position
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = velocity
        self.lastUpdated = time_ns()

    def update(self):
        delta = (time_ns() - self.lastUpdated) / 1e9
        self.lastUpdated = time_ns()
        self.position = (
            self.position[0] + self.velocity[0] * delta,
            self.position[1] + self.velocity[1] * delta,
        )

        if self.position[0] < X_LOWER_LIM:
            self.position = (
                X_UPPER_LIM,
                random.randint(Y_LOWER_LIM, Y_UPPER_LIM),
            )
            self.velocity = (random.randint(-250, -200), 0)

        # Update rect.
        self.rect = self.image.get_rect(center=self.position)
