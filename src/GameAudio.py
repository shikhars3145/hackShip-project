import pygame


class GameAudio:
    def __init__(self, channel):
        self.channel = channel

    def playFX(self, filename, volume):
        sound = pygame.mixer.Sound(filename)
        sound.set_volume(volume)
        channel = pygame.mixer.Channel(self.channel)
        channel.play(sound, loops=0, maxtime=0, fade_ms=0)

    def playLooped(self, filename, volume, count: int = -1):
        sound = pygame.mixer.Sound(filename)
        sound.set_volume(volume)
        channel = pygame.mixer.Channel(self.channel)
        channel.play(sound, loops=count, maxtime=0, fade_ms=6000)

    def stop(self):
        channel = pygame.mixer.Channel(self.channel)
        channel.fadeout(1000)

    def queue(self, filename, volume):
        sound = pygame.mixer.Sound(filename)
        sound.set_volume(volume)
        channel = pygame.mixer.Channel(self.channel)
        channel.queue(sound)

    def is_busy(self):
        channel = pygame.mixer.Channel(self.channel)
        return channel.get_busy()
