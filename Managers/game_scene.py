import pygame
import Managers.sound_manager as sound_manager
from Managers.scene_manager import MainScene

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
        pygame.display.set_caption("飞机Dark战")
