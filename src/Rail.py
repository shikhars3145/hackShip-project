import pygame
from typing import List, Tuple
from resource import getResource


class RailSprite(pygame.sprite.Sprite):
    def __init__(
        self, image, position: Tuple[float, float],
    ):
        super().__init__()
        self.image = image
        self.position = position
        self.rect = self.image.get_rect(topleft=position)

    def update(self, translate: float):
        self.translate(translate)

    def translate(self, amount: float):
        self.position = (self.position[0] + amount, self.position[1])
        self.rect = self.image.get_rect(topleft=self.position)


class Rail(pygame.sprite.RenderPlain):
    def __init__(
        self,
        position: Tuple[float, float],
        limit: float,
        speed: float,
        images: List,
    ):
        super().__init__()
        self.position = position
        self.limit = limit
        self.speed = speed
        self.images = images
        offset = 0
        for image in images:
            self.add(RailSprite(image, (position[0] + offset, position[1])))
            offset += image.get_width()

    def update(self, delta: float):
        distance = self.speed * delta
        totalWidth = 0
        for sprite in self.sprites():
            totalWidth += sprite.image.get_width()
        super().update(distance)
        for sprite in self.sprites():
            if sprite.position[0] <= self.limit:
                sprite.translate(totalWidth)


class ForegroundRail(Rail):
    def __init__(
        self, position: Tuple[float, float], limit: float, speed: float
    ):
        source = pygame.image.load(
            getResource("images/underwater-fantasy/foreground-merged.png")
        )
        images = [source] * 5
        super().__init__(position, limit, speed, images)


class MiddlegroundRail(Rail):
    def __init__(
        self, position: Tuple[float, float], limit: float, speed: float
    ):
        source = pygame.image.load(
            getResource("images/underwater-fantasy/sand.png")
        )
        source = pygame.transform.scale2x(source)
        images = [source] * 5
        super().__init__(position, limit, speed, images)


class BackgroundRail(Rail):
    def __init__(
        self, position: Tuple[float, float], limit: float, speed: float
    ):
        source = pygame.image.load(
            getResource("images/underwater-fantasy/far.png")
        )
        source = pygame.transform.scale2x(source)
        source = pygame.transform.scale2x(source)
        images = [source] * 3
        super().__init__(position, limit, speed, images)
