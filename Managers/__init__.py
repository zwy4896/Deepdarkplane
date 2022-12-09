#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Author      : Bluzy
Date        : 2022/12/09 14:13:44
Contact     : zoe4896@outlook.com
Description : 
'''

from .action import *
from .game_scene import GameScene
from Characters import *
from Managers.scene_manager import MainSceneFactory
from Managers.game_scene import GameScene

class Manager():
    def __init__(self) -> None:
        main_scene = MainSceneFactory()
        self.scene = main_scene.get_scene('initial')
        GameScene(self.scene)
        self.player = Player(0, 0, 0)
        self.invoke = Invoke()
