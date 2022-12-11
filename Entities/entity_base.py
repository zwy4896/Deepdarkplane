#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Author      : Bluzy
Date        : 2022/12/10 19:17:59
Contact     : zoe4896@outlook.com
Description : 
'''

import pygame
from Utils.math import Pos2D

class EntityBase():
    def __init__(self, position: Pos2D) -> None:
        self.rect = pygame.Rect(position.x)