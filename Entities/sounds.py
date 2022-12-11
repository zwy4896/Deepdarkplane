#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
File        : sounds.py
Description : 
Date        : 2021/11/13 10:00:30
Author      : Bluzy
'''
from abstract.game_entity_abc import SoundEntity
import pygame

class Sounds(SoundEntity):
    def sound(self, fileName, volume):
        asset = pygame.mixer.Sound(fileName)
        asset.set_volume(volume)

        return asset
    def sound_loop(self, fileName, volume):
        pygame.mixer.music.load(fileName)
        pygame.mixer.music.set_volume(volume)