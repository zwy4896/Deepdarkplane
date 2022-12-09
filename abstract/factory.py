#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Author      : Bluzy
Date        : 2022/12/09 21:37:30
Contact     : zoe4896@outlook.com
Description : Abstract factory
'''

from abc import ABC, abstractmethod

class SceneFactory(ABC):
    @abstractmethod
    def get_scene(self):
        pass

class TraitFactory(ABC):
    @abstractmethod
    def get_trait(self):
        pass