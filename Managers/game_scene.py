import pygame
import Managers.sound_manager as sound_manager
from Managers.scene_manager import MainScene
from Configs.config import *

class GameScene():
    def __init__(self, scene) -> None:
        super().__init__()
        self.engin_init()
        scene.create_background()
        scene.create_audio()
        scene.create_button()
        scene.create_font()
        # self.init()
        # self.init_scene()
        # self.init_sounds()
        # self.init_button()
        # self.init_font()
        # self.bgm_play()
        pygame.mixer.music.play(-1)
        
    def engin_init(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(CAPTION)

    def update(self, scene):
        scene.screen.blit(scene.background,(0,0))
        cp_info_text = scene.cp_info_font.render('Made by'.format(AUTHOR), True, BLACK)
        scene.screen.blit(cp_info_text, (200, 650))
        scene.strt_rect.left, scene.strt_rect.top = 150, 200
        scene.screen.blit(scene.strt_image, scene.strt_rect)

        scene.help_rect.left, scene.help_rect.top = 150, 290
        scene.screen.blit(scene.help_image, scene.help_rect)
