#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Author      : Bluzy
Date        : 2022/12/09 14:12:20
Contact     : zoe4896@outlook.com
Description : 
'''

from Characters import Player
import Managers
from Managers.scene_manager import MainSceneFactory
from Managers.game_scene import GameScene

if __name__ == '__main__':
    # player = Player(0,0,0)
    # invoke = Managers.Invoke()
    # move_up = Managers.MoveUpCommand()
    # move_down = Managers.MoveDownCommand()
    # invoke.add_commands(move_up)
    # invoke.add_commands(move_up)
    # invoke.add_commands(move_down)
    # invoke.execute_command(player)

    main_scene = MainSceneFactory()
    scene = main_scene.get_scene('lv2')
    main = GameScene(scene)
    main.init_scene()