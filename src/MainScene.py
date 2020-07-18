from Scene import Scene
from config import SCREEN_HEIGHT
from Player import Player
from Garbage import Garbage
from GameAudio import GameAudio
import pygame

BMG_LOOP = 'src/assets/audio/bgmLoop.wav'
TRASH_BOTTLE = 'src/assets/audio/trashBottle.wav'

class MainScene(Scene):
    gameMusic = GameAudio(1)
    trashFXbottle = GameAudio(2)
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

        # Scoring
        self.scoreInt = 0
        self.scoreFont = pygame.font.Font('src/assets/fonts/Lato/Lato-Black.ttf', 32)

        # Audio
        self.gameMusic.playLooped(BMG_LOOP, 0.3)

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
        # Render score
        screen.blit(self.scoreFont.render(str(self.scoreInt), True, (255, 255, 255)), (20, 20))


    def checkCollision(self):
        for garbageInstance in self.garbageGroup:
            if pygame.sprite.collide_mask(self.player, garbageInstance):
                self.scoreInt += 1
                self.trashFXbottle.playFX(TRASH_BOTTLE, 0.15)
                garbageInstance.reset()
