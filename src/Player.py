import pygame
from typing import Tuple


# Player sprite.
class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        position: Tuple[float, float],
        velocity: Tuple[float, float] = (0, 0)
    ):
        super().__init__()
        self.image = pygame.image.load("src/assets/images/player.png")
        self.position = position
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)
        self.velocity = velocity
        self.DECCEL_VAL = 0.99

    def update(self):
        self.accelerate(self.accel)
        if self.accel == 0:
            self.deccelerate()
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
        )
        self.rect = self.image.get_rect(center=self.position)

    # Accelerate when keyboard up is pressed
    def accelerate(self, change):
        self.velocity = (
            self.velocity[0],
            self.velocity[1] + change
        )

    def deccelerate(self):
        self.velocity = (
            self.velocity[0],
            self.velocity[1] * self.DECCEL_VAL
        )
