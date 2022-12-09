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
import threading

class mouse_thread(threading.Thread):
    def __init__(self) -> None:
        threading.Thread.__init__(self)
    
    def run(self) -> None:
        return super().run()

def main():
    clock = pygame.time.Clock()
    #生成开始界面
    run = False
    manager = Manager()
    scene = manager.scene
    game_scene = manager.game_scene
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
        game_scene.update(scene)

        #检测鼠标操作
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            if scene.strt_rect.left < pos[0] < scene.strt_rect.right and \
                scene.strt_rect.top < pos[1] < scene.strt_rect.bottom:
                run = True
                

            elif scene.help_rect.left < pos[0] < scene.help_rect.right and \
                    scene.help_rect.top < pos[1] < scene.help_rect.bottom:
                scene.screen.blit(scene.help_text, scene.help_text_rect)
        
        #暂停按钮
        scene.screen.blit(paused_image, scene.paused_rect)
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
