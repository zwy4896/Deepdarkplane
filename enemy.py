import pygame
from random import *


#小型敌机
class SmlEnemy(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/sm_enm1.png").convert_alpha()
        self.image2 = pygame.image.load("images/sm_enm.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/sml_down1.png"),\
            pygame.image.load("images/sml_down2.png"),\
            pygame.image.load("images/sml_down3.png"),\
            pygame.image.load("images/sml_down4.png")\
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0],bg_size[1]
        self.speed = 2
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0,self.width - self.rect.width),\
                        randint(-5 * self.height, 0)
        self.mask = pygame.mask.from_surface(self.image1)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()


    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0,self.width - self.rect.width),\
                        randint(-5 * self.height, 0)
#中型敌机
class MidEnemy(pygame.sprite.Sprite):
    energy = 8
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/mid_enm.png").convert_alpha()
        self.image2 = pygame.image.load("images/mid_enm1.png").convert_alpha()
        self.image3 = pygame.image.load("images/mid_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/mid_down1.png"),\
            pygame.image.load("images/mid_down2.png"),\
            pygame.image.load("images/mid_down3.png"),\
            pygame.image.load("images/mid_down4.png")\
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0],bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0,self.width - self.rect.width),\
                        randint(-10 * self.height, -self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = MidEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()


    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0,self.width - self.rect.width),\
                        randint(-10 * self.height, -self.height)

#大型敌机
class BigEnemy(pygame.sprite.Sprite):
    energy = 15
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/big_enm.png")
        self.image2 = pygame.image.load("images/big_enm1.png")
        self.image3 = pygame.image.load("images/boss_hit.png")
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/big_down1.png"),\
            pygame.image.load("images/big_down2.png"),\
            pygame.image.load("images/big_down3.png"),\
            pygame.image.load("images/big_down4.png")\
            ])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0],bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0,self.width - self.rect.width),\
                        randint(-15 * self.height, -5 * self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = BigEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()


    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
                        randint(0,self.width - self.rect.width),\
                        randint(-15 * self.height, -5 * self.height)
