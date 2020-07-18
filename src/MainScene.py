from Scene import Scene
from config import SCREEN_HEIGHT
from Player import Player
from Garbage import Garbage
import pygame


class MainScene(Scene):
    def __init__(self):
        super().__init__()

        # Player
        self.player = Player((30, (SCREEN_HEIGHT - 64) / 2))
        self.playerGroup = pygame.sprite.RenderPlain(self.player)

        # Garbage
        self.garbageGroup = pygame.sprite.RenderPlain()
        for i in range(5):
            self.garbage = Garbage()
            self.garbageGroup.add(self.garbage)

    def handleEvent(self, event):
        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player.accel -= self.player.ACCEL_CONST
            if event.key == pygame.K_DOWN:
                self.player.accel += self.player.ACCEL_CONST

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.player.accel = 0

    def render(self, screen):
        self.playerGroup.update()
        self.garbageGroup.update()
        # Render Player
        self.playerGroup.draw(screen)
        # Render Garbage
        self.garbageGroup.draw(screen)

    
    def checkCollision(self):
        for garbageInstance in self.garbageGroup:
            if pygame.sprite.collide_mask(self.player, garbageInstance):
                garbageInstance.reset()
    

