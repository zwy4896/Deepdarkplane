import pygame as pg
import random
from settings import *
import player

class Game:
    # Initialize game and create window
    def __init__(self):
        self.bkimg = pg.image.load("images/bg.png")
        self.running = True
        self.bg_size = width, height
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(self.bg_size)
        pg.display.set_caption(NAME)
        self.clock = pg.time.Clock()

    def new(self):
        # Start new game
        self.all_sprites = pg.sprite.Group()
    #     Create player
        self.player = player.Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # main loop
        self.playing = True
        # While playing, do events(), update(), draw()
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop update
        self.all_sprites.update()

    def events(self):
        # Listening events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Drawing
        self.screen.blit(self.bkimg,(0,0))
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def show_start_screen(self):
#         Show start screen
        pass

    def show_gameOver_screen(self):
#         show game over screen
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_gameOver_screen()

pg.quit()