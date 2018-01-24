import pygame

class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image0 = pygame.image.load("images/bullet0.png").convert_alpha()
        self.image1 = pygame.image.load("images/bullet1.png").convert_alpha()
        self.rect = self.image0.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 3
        self.active = True
        self.mask = pygame.mask.from_surface(self.image0)
        self.mask = pygame.mask.from_surface(self.image1)

    def move(self):
        self.rect.top -= self.speed

        if self.rect.top < 0:
            self.active = False

    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
