import pygame
import random
from typing import Tuple, Set
from config import X_LOWER_LIM
from os import walk
from os.path import join
from KinemeticBody import KinematicBody

GARBAGE_IMAGES: Set[str] = set()
for (dirpath, _, filenames) in walk("src/assets/images/garbage"):
    for filename in filenames:
        GARBAGE_IMAGES.add(join(dirpath, filename))


def getRandomGarbageImagePath():
    return random.sample(GARBAGE_IMAGES, 1)[0]


# Player sprite.
class Garbage(KinematicBody):
    def __init__(
        self,
        position: Tuple[float, float],
        velocity: Tuple[float, float] = None,
    ):
        if velocity is None:
            velocity = (random.randint(-150, -100), 0)
        super().__init__(
            pygame.image.load(getRandomGarbageImagePath()), position, velocity
        )

    def update(self, delta: float):
        super().update(delta)

        # Boundary check.
        if self.position[0] < X_LOWER_LIM:
            self.kill()
