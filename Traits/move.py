#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Author      : Bluzy
Date        : 2022/12/10 00:05:15
Contact     : zoe4896@outlook.com
Description : 
'''

class MoveTraits():
    def __init__(self, entity) -> None:
        self.direction = -1
        self.entity = entity
        self.speed = 3

    def update(self):
        pass
