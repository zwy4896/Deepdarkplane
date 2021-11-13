import pygame
import os
import manager.sound_manager as sound_manager

class GameScene(object):
    def __init__(self) -> None:
        super().__init__()
        self.init()
        self.init_scene()
        self.init_sounds()
    
    def init(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("飞机Dark战")

    def init_scene(self):
        self.bg_size = width, height = 480, 700
        self.screen = pygame.display.set_mode(self.bg_size)
        self.background = pygame.image.load("assets/images/bg.png").convert()
        print('游戏场景初始化完毕!')

    def init_sounds(self):
        sound_manager.get_bgm('assets/sounds/loop.wav', 1)
        self.boss_flight_sound = sound_manager.get_sound('assets/sounds/boss.wav', 1)
        self.boss_down_sound = sound_manager.get_sound('assets/sounds/boss_down_sound.wav', 1.5)
        self.down_sound = sound_manager.get_sound('assets/sounds/down_sound.wav', 1)
        self.lvl_upd_sound = sound_manager.get_sound('assets/sounds/lvl_upd.wav', 1)
        print('声音加载完毕!')
    
