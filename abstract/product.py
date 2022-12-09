#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Author      : Bluzy
Date        : 2022/12/09 21:40:49
Contact     : zoe4896@outlook.com
Description : Abstract products
'''

from abc import ABC, abstractmethod

class BackGround(ABC):
    @abstractmethod
    def create_background(self):
        pass

class Audio(ABC):
    @abstractmethod
    def create_audio(self):
        pass
    