import pygame
import random
from typing import Tuple, Set
from time import time_ns
from config import (
    X_LOWER_LIM,
    X_UPPER_LIM,
    Y_LOWER_LIM,
    Y_UPPER_LIM,
)
from os import walk
from os.path import join

GARBAGE_IMAGES: Set[str] = set()
for (dirpath, _, filenames) in walk("src/assets/images/garbage"):
    for filename in filenames:
        GARBAGE_IMAGES.add(join(dirpath, filename))


def getRandomGarbageImagePath():
    return random.sample(GARBAGE_IMAGES, 1)[0]


# Player sprite.
class Garbage(pygame.sprite.Sprite):
    def __init__(
        self,
        position: Tuple[float, float],
        velocity: Tuple[float, float] = None,
    ):
        super().__init__()
        self.image = pygame.image.load(getRandomGarbageImagePath())
        self.position = position
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)
        if velocity is None:
            self.velocity = (random.randint(-150, -100), 0)
        else:
            self.velocity = velocity
        self.lastUpdated = time_ns()

    def update(self):
        # Constantly move garbage to left
        delta = (time_ns() - self.lastUpdated) / 1e9
        self.lastUpdated = time_ns()

        self.position = (
            self.position[0] + self.velocity[0] * delta,
            self.position[1] + self.velocity[1] * delta,
        )

        if self.position[0] < X_LOWER_LIM:
            self.kill()

        # Update rect.
        self.rect = self.image.get_rect(center=self.position)
