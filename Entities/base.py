import pygame

class Base(object):
    def __init__(self, screen, x, y, imageName) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(imageName)
