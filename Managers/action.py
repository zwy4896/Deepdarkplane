#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Author      : Bluzy
Date        : 2022/12/09 13:33:18
Contact     : zoe4896@outlook.com
Description : 
'''

from abstract import Command

class MoveUpCommand(Command):
    def execute(self, actor):
        actor.move_up()

class MoveDownCommand(Command):
    def execute(self, actor):
        actor.move_down()
        
class MoveLeftCommand(Command):
    def execute(self, actor):
        actor.move_left()

class MoveRightCommand(Command):
    def execute(self, actor):
        actor.move_right()

class Invoke():
    def __init__(self) -> None:
        self.commands = []

    def clear_command(self):
        self.commands.clear()
    def add_commands(self, command):
        self.commands.append(command)
    
    def execute_command(self, actor):
        for command in self.commands:
            command.execute(actor)