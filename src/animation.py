import pygame


def splitImage(image, row_count: int, column_count: int):
    """Split sprite sheet into individual frames."""
    originalWidth = image.get_width()
    originalHeight = image.get_height()
    frameWidth = originalWidth // column_count
    frameHeight = originalHeight // row_count
    frame = pygame.Surface(
        (frameWidth, frameHeight), pygame.SRCALPHA, 32
    )
    ret = []
    for i in range(row_count * column_count):
        row = i // column_count
        column = i % column_count
        frame.fill((255, 255, 255, 0))
        frame.blit(
            image,
            (0, 0),
            (frameWidth * column, frameHeight * row, frameWidth, frameHeight)
        )
        ret.append(frame.copy())
    return ret
