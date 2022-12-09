#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
File        : Fight.py
Description : 
Date        : 2022/12/07 23:35:31
Author      : Bluzy
'''


import pygame
import sys
import traceback
import myplane
import enemy
import bullet
from pygame.locals import *
from random import *
from Managers import Manager

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def main():
    clock = pygame.time.Clock()
    #生成开始界面
    run = False
    manager = Manager()
    scene = manager.scene
    invoke = manager.invoke
    
    running = True
    paused = False


    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and scene.paused_rect.collidepoint(event.pos):
                    paused = not paused

            elif event.type == MOUSEMOTION:
                if scene.paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = scene.resume_prs_image
                    else:
                        paused_image = scene.pause_prs_image
                else:
                    if paused:
                        paused_image = scene.resume_nor_image
                    else:
                        paused_image = scene.pause_nor_image
        #绘制开始界面
        scene.screen.blit(scene.background,(0,0))
        cp_info_text = scene.cp_info_font.render("Made by Bluzy", True, BLACK)
        scene.screen.blit(cp_info_text, (200, 650))
        scene.strt_rect.left, scene.strt_rect.top = 150, 200
        scene.screen.blit(scene.strt_image, scene.strt_rect)

        scene.help_rect.left, scene.help_rect.top = 150, 290
        scene.screen.blit(scene.help_image, scene.help_rect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
