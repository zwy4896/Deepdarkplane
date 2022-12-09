#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Author      : Bluzy
Date        : 2022/12/09 13:11:31
Contact     : zoe4896@outlook.com
Description : 
'''

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, actor):
        raise NotImplementedError