# Game settings
import pygame as pg

vec = pg.math.Vector2

width = 480
height = 360
FPS = 60
NAME = "Alpha"

# Define colours
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PLAYER_POS_INI = vec(300, 300)
PLAYER_ACC_INI = vec(0, 0.98)
PLAYER_SPEED = 8