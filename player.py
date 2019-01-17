import pygame as pg
from settings import *

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # Player animation
        self.image = pg.image.load("images/wang.png").convert_alpha()

        # Player died

        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = PLAYER_POS_INI

        # Speed
        self.speed = vec(0, 0)

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= PLAYER_SPEED
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < width:
            self.rect.left += PLAYER_SPEED
        else:
            self.rect.right = width

    def update(self):
        # Move player
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.moveLeft()
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.moveRight()