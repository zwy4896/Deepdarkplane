#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Author      : Bluzy
Date        : 2022/12/09 13:52:15
Contact     : zoe4896@outlook.com
Description : 
'''
import pygame
from Utils import singleton

@singleton
class Player(pygame.sprite.Sprite):
    def __init__(self, init_pos, speed, animation) -> None:
        self.__init_pos = init_pos
        self.speed = speed
        self.animation = animation
    def move_up(self):
        self.print_message('move up!')
    def move_down(self):
        self.print_message('move down!')
    def move_left(self):
        self.print_message('move left!')
    def move_right(self):
        self.print_message('move right!')
    
    def print_message(self, content):
        print("{} --> {}".format(self.__class__.__name__, content))
