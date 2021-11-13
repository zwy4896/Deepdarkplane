from abc import abstractmethod, ABCMeta
import pygame

class SoundEntity(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def sound(self):
        return