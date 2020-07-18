import pygame
from typing import Tuple


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

    def update(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
        )
        self.rect = self.image.get_rect(center=self.position)
