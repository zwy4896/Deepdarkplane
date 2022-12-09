#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Author      : Bluzy
Date        : 2022/12/09 15:00:44
Contact     : zoe4896@outlook.com
Description : 
'''

def singleton(cls):
    _instance = {}
    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args)
        return _instance[cls]

    return inner