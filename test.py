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

if __name__ == '__main__':
    player = Player(0,0,0)
    invoke = Managers.Invoke()
    move_up = Managers.MoveUpCommand()
    move_down = Managers.MoveDownCommand()
    invoke.add_commands(move_up)
    invoke.add_commands(move_up)
    invoke.add_commands(move_down)
    invoke.execute_command(player)