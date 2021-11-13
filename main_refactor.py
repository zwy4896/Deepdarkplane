#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
File        : main_refactor.py
Description : 
Date        : 2021/11/13 13:50:25
Author      : Bluzy
'''


import pygame
import sys
import traceback
import myplane
import enemy
import bullet
from pygame.locals import *
from random import *
from manager import game_scene

def main():
    # 初始化游戏场景
    scene = game_scene.GameScene()
    

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()