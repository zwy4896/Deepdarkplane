import pygame
import os
import Managers.sound_manager as sound_manager

class GameScene(object):
    def __init__(self) -> None:
        super().__init__()
        self.init()
        self.init_scene()
        self.init_sounds()
        self.init_button()
        self.init_font()
        pygame.mixer.music.play(-1)
    
    def init(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("飞机Dark战")

    def init_button(self):
        self.pause_nor_image = pygame.image.load("assets/images/pause_nor.png").convert_alpha()
        self.pause_prs_image = pygame.image.load("assets/images/pause_prs.png").convert_alpha()
        self.resume_nor_image = pygame.image.load("assets/images/resume_nor.png").convert_alpha()
        self.resume_prs_image = pygame.image.load("assets/images/resume_prs.png").convert_alpha()
        self.paused_rect = self.pause_nor_image.get_rect()
        self.paused_rect.left, self.paused_rect.top = self.width - self.paused_rect.width - 10, 10
        self.paused_image = self.pause_nor_image
        print('按钮初始化完毕!')

    def init_font(self):
        self.score_font = pygame.font.Font("assets/fonts/STCAIYUN.TTF",36)
        self.cp_info_font = pygame.font.Font("assets/fonts/GIGI.TTF",28)
        self.level_font = pygame.font.Font("assets/fonts/GIGI.TTF",36)
        self.gmov_font = pygame.font.Font("assets/fonts/GIGI.TTF",48)
        print('字体加载完毕!')

    def init_scene(self):
        self.bg_size = self.width, self.height = 480, 700
        self.screen = pygame.display.set_mode(self.bg_size)
        self.background = pygame.image.load("assets/images/bg.png").convert()
        self.strt_image = pygame.image.load("assets/images/strt.png").convert_alpha()
        self.strt_rect = self.strt_image.get_rect()

        self.help_image = pygame.image.load("assets/images/help.png").convert_alpha()
        self.help_rect = self.help_image.get_rect()

        #帮助界面
        self.help_text = pygame.image.load("assets/images/help_text1.png").convert_alpha()
        self.help_text_rect = self.help_text.get_rect()
        # self.game_scene()
        print('游戏场景初始化完毕!')

    def init_sounds(self):
        sound_manager.get_bgm('assets/sounds/loop.wav', 1)
        self.boss_flight_sound = sound_manager.get_sound('assets/sounds/boss.wav', 1)
        self.boss_down_sound = sound_manager.get_sound('assets/sounds/boss_down_sound.wav', 1.5)
        self.down_sound = sound_manager.get_sound('assets/sounds/down_sound.wav', 1)
        self.lvl_upd_sound = sound_manager.get_sound('assets/sounds/lvl_upd.wav', 1)
        print('声音加载完毕!')
    
    def game_scene(self):
        self.strt_image = pygame.image.load("assets/images/strt.png").convert_alpha()
        self.strt_rect = self.strt_image.get_rect()

        self.help_image = pygame.image.load("assets/images/help.png").convert_alpha()
        self.help_rect = self.help_image.get_rect()

        #帮助界面
        self.help_text = pygame.image.load("assets/images/help_text1.png").convert_alpha()
        self.help_text_rect = self.help_text.get_rect()
        self.again_image = pygame.image.load("assets/images/again.png").convert_alpha()
        self.again_rect = self.again_image.get_rect()
        self.gmov_image = pygame.image.load("assets/images/gmov.png").convert_alpha()
        self.gmov_rect = self.gmov_image.get_rect()
    def bgm_play(self):
        pygame.mixer.music.play(-1)