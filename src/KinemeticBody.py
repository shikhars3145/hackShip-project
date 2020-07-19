import pygame
from typing import Tuple


class KinematicBody(pygame.sprite.Sprite):
    """Sprite with physical properties"""
    def __init__(
        self,
        image,
        position: Tuple[float, float],
        velocity: Tuple[float, float] = (0, 0),
        acceleration: Tuple[float, float] = (0, 0)
    ):
        super().__init__()
        self.image = image
        self.position = position
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(image)
        self.velocity = velocity
        self.acceleration = acceleration

    def update(self, delta: float):
        self.velocity = (
            self.velocity[0] + self.acceleration[0] * delta,
            self.velocity[1] + self.acceleration[1] * delta
        )
        self.position = (
            self.position[0] + self.velocity[0] * delta,
            self.position[1] + self.velocity[1] * delta
        )
        self.rect = self.image.get_rect(center=self.position)
