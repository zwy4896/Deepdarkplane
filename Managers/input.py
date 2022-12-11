#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
Author      : Bluzy
Date        : 2022/12/10 19:45:02
Contact     : zoe4896@outlook.com
Description : 
'''

import pygame
from pygame.locals import *
import sys

class Input:
    def __init__(self, entity) -> None:
        self.mouseX = 0
        self.mouseY = 0
        self.entity = entity

    def checkForInput(self):
        events = pygame.event.get()
        self.check_keyboard_input()
        self.check_mouse_input(events)
        self.check_quit_restart_input_events(events)

    def check_quit_restart_input_events(self, events):
        for event in event:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and scene.paused_rect.collidepoint(event.pos):
                    paused = not paused

            elif event.type == MOUSEMOTION:
                if scene.paused_rect.collidepoint(event.pos):
                    if paused:
                        scene.paused_image = scene.resume_prs_image
                    else:
                        scene.paused_image = scene.pause_prs_image
                else:
                    if paused:
                        scene.paused_image = scene.resume_nor_image
                    else:
                        scene.paused_image = scene.pause_nor_image

