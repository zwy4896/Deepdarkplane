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
from manager import game_scene

scene = game_scene.GameScene()
bg_size = scene.bg_size
width, height = scene.width, scene.height

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def add_sml_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmlEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

def inc_speed(target, inc):
    for each in target:
        each.speed += inc
        

def main():
    #生成开始界面
    run = False
    scene = game_scene.GameScene()
    scene.game_scene()
    
    lvl_upd_sound = scene.lvl_upd_sound
    screen = scene.screen
    background = scene.background
    boss_flight_sound = scene.boss_flight_sound
    boss_down_sound = scene.boss_down_sound
    down_sound = scene.down_sound
    strt_rect = scene.strt_rect
    strt_image = scene.strt_image
    help_image = scene.help_image
    help_rect = scene.help_rect
    help_text = scene.help_text
    help_text_rect = scene.help_text_rect
    #生成我方飞机
    me = myplane.MyPlane(bg_size)

    enemies = pygame.sprite.Group()

    #生成小型敌机
    sml_enemies = pygame.sprite.Group()
    add_sml_enemies(sml_enemies,enemies,16)

    #中型敌机
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,8)

    #大型敌机
    big_enemies = pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,4)

    #生成子弹
    bullet1 = []
    bullet1_idx = 0
    BULLET1_NUM = 20
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.topleft))
    
    clock = pygame.time.Clock()

    

    #中弹图片索引
    sml_dst_idx = 0
    mid_dst_idx = 0
    big_dst_idx = 0
    me_dst_idx = 0

    #计分板
    score = 0
    score_font = pygame.font.Font("assets/fonts/STCAIYUN.TTF",36)

    cp_info_font = pygame.font.Font("assets/fonts/GIGI.TTF",28)

    #暂停游戏
    paused = False
    pause_nor_image = pygame.image.load("assets/images/pause_nor.png").convert_alpha()
    pause_prs_image = pygame.image.load("assets/images/pause_prs.png").convert_alpha()
    resume_nor_image = pygame.image.load("assets/images/resume_nor.png").convert_alpha()
    resume_prs_image = pygame.image.load("assets/images/resume_prs.png").convert_alpha()
    paused_rect = pause_nor_image.get_rect()
    paused_rect.left, paused_rect.top = width - paused_rect.width - 10, 10
    paused_image = pause_nor_image

    #设置难度
    level = 1

    #等级信息
    level_font = pygame.font.Font("assets/fonts/GIGI.TTF",36)

    #生命数量
    life_num = 1

    #GameOver画面
    gmov_font = pygame.font.Font("assets/fonts/GIGI.TTF",48)
    again_image = pygame.image.load("assets/images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gmov_image = pygame.image.load("assets/images/gmov.png").convert_alpha()
    gmov_rect = gmov_image.get_rect()

    #阻止重复打开记录文件
    recorded = False
    
    #切换飞机状态图片
    switch_image = True

    #延迟
    delay = 100
    
    running = True

    while running:        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and paused_rect.collidepoint(event.pos):
                    paused = not paused

            elif event.type == MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image = resume_prs_image
                    else:
                        paused_image = pause_prs_image
                else:
                    if paused:
                        paused_image = resume_nor_image
                    else:
                        paused_image = pause_nor_image


        #增加难度
        if level == 1 and score >= 3:
            level = 2
            lvl_upd_sound.play()
            #增加三架小型敌机，两架中，2架大
            add_sml_enemies(sml_enemies, enemies, 3)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 2)
            #加速
            inc_speed(sml_enemies, 1)

        elif level == 2 and score >= 8:
            level = 3
            lvl_upd_sound.play()
            #增加4架小型敌机，2架中，2架大
            add_sml_enemies(sml_enemies, enemies, 4)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 2)
            #加速小
            inc_speed(sml_enemies, 1)
            #加速中
            inc_speed(mid_enemies, 1)
        elif level == 3 and score >= 15:
            level = 4
            lvl_upd_sound.play()
            #增加三架小型敌机，两架中，2架大
            add_sml_enemies(sml_enemies, enemies, 5)
            add_mid_enemies(mid_enemies, enemies, 2)
            add_big_enemies(big_enemies, enemies, 2)
            #加速小
            inc_speed(sml_enemies, 1)
            #加速中
            inc_speed(mid_enemies, 1)

        
        #绘制开始界面
        screen.blit(background,(0,0))

        cp_info_text = cp_info_font.render("Made by Bluzy", True, BLACK)
        screen.blit(cp_info_text, (200, 650))
        strt_rect.left, strt_rect.top = 150, 200
        screen.blit(strt_image, strt_rect)

        help_rect.left, help_rect.top = 150, 290
        screen.blit(help_image, help_rect)

        #检测鼠标操作
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            if strt_rect.left < pos[0] < strt_rect.right and \
                strt_rect.top < pos[1] < strt_rect.bottom:
                run = True
                

            elif help_rect.left < pos[0] < help_rect.right and \
                    help_rect.top < pos[1] < help_rect.bottom:
                screen.blit(help_text, help_text_rect)
        
        if run:
            screen.blit(background,(0,0))
            if life_num and not paused:
                #检测键盘操作
                key_pressed = pygame.key.get_pressed()
                
                if key_pressed[K_w] or key_pressed[K_UP]:
                    me.moveUp()
                if key_pressed[K_s] or key_pressed[K_DOWN]:
                    me.moveDown()
                if key_pressed[K_a] or key_pressed[K_LEFT]:
                    me.moveLeft()
                if key_pressed[K_d] or key_pressed[K_RIGHT]:
                    me.moveRight()

                #空格键发射子弹
                if key_pressed[K_SPACE]:
                    #发射子弹
                    if not(delay % 20):
                        bullet1[bullet1_idx].reset(me.rect.topleft)
                        bullet1[bullet1_idx].active = True
                        bullet1_idx = (bullet1_idx + 1) % BULLET1_NUM
                    

                #击中检测
                for b in bullet1:
                    if b.active:
                        b.move()
                        if switch_image:
                            screen.blit(b.image0, b.rect)
                        else:
                            screen.blit(b.image1, b.rect)
                        enm_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                        if enm_hit:
                            b.active = False
                            for e in enm_hit:
                                if e in mid_enemies or e in big_enemies:
                                    e.hit = True
                                    e.energy -= 1
                                    if e.energy == 0:
                                        e.active = False
                                else:
                                    e.active = False

        
                #绘制大型敌机
                for each in big_enemies:
                    if each.active:
                        each.move()
                        if each.hit:
                            screen.blit(each.image3,each.rect)
                            each.hit = False
                        else:
                            if switch_image:
                                screen.blit(each.image1, each.rect)
                            else:
                                screen.blit(each.image2, each.rect)

                        #绘制血槽
                        pygame.draw.line(screen, BLACK,\
                                         (each.rect.left, each.rect.top - 5),\
                                         (each.rect.right, each.rect.top -5),\
                                         2)

                        #大于20%显示绿色，否则红色
                        energy_remain = each.energy / enemy.BigEnemy.energy
                        if energy_remain > 0.2:
                            energy_color = GREEN
                        else:
                            energy_color = RED
                        pygame.draw.line(screen, energy_color,\
                                         (each.rect.left, each.rect.top - 5),\
                                         (each.rect.left + each.rect.width * energy_remain,\
                                          each.rect.top - 5),2)
                        #大敌机出场BGM
                        if each.rect.bottom == -50:
                            boss_flight_sound.play()
                    else:
                        #毁灭
                        if not(delay % 3):
                            if big_dst_idx == 0:
                                boss_down_sound.play()
                            screen.blit(each.destroy_images[big_dst_idx],each.rect)
                            big_dst_idx = (big_dst_idx + 1) % 4
                            if big_dst_idx == 0:
                                boss_flight_sound.stop()
                                score += 10
                                each.reset()
                            

                #中型敌机
                for each in mid_enemies:
                    if each.active:
                        each.move()
                        if each.hit:
                            screen.blit(each.image3,each.rect)
                            each.hit = False
                        else:
                            if switch_image:
                                screen.blit(each.image1, each.rect)
                            else:
                                screen.blit(each.image2, each.rect)

                        #血槽
                        pygame.draw.line(screen, BLACK,\
                                         (each.rect.left, each.rect.top - 5),\
                                         (each.rect.right, each.rect.top -5),\
                                         2)

                        #大于20%显示绿色，否则红色
                        energy_remain = each.energy / enemy.MidEnemy.energy
                        if energy_remain > 0.2:
                            energy_color = GREEN
                        else:
                            energy_color = RED
                        pygame.draw.line(screen, energy_color,\
                                         (each.rect.left, each.rect.top - 5),\
                                         (each.rect.left + each.rect.width * energy_remain,\
                                          each.rect.top - 5),2)
                    else:
                        #毁灭
                        if not(delay % 3):
                            if mid_dst_idx == 0:
                                down_sound.play()
                            screen.blit(each.destroy_images[mid_dst_idx],each.rect)
                            mid_dst_idx = (mid_dst_idx + 1) % 4
                            if mid_dst_idx == 0:
                                score += 5
                                each.reset()

                #小型敌机
                for each in sml_enemies:
                    if each.active:
                        each.move()
                        if switch_image:
                            screen.blit(each.image1, each.rect)
                        else:
                            screen.blit(each.image2, each.rect)
                    else:
                        #毁灭
                        if not(delay % 3):
                            if sml_dst_idx == 0:
                                down_sound.play()
                            screen.blit(each.destroy_images[sml_dst_idx],each.rect)
                            sml_dst_idx = (sml_dst_idx + 1) % 4
                            if sml_dst_idx == 0:
                                score -= 1
                                each.reset()

                #碰撞检测
                enm_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
                if enm_down:
                    me.active = False  #注释此处可作弊^_^
                    for e in enm_down:
                        e.active = False
                        
                #绘制我方飞机
                if me.active:
                    if switch_image:
                        screen.blit(me.image1, me.rect)
                    else:
                        screen.blit(me.image2, me.rect)
                else:
                    #毁灭
                    
                    if not(delay % 3):
                        if me_dst_idx == 0:
                            down_sound.play()
                        screen.blit(each.destroy_images[me_dst_idx],each.rect)
                        me_dst_idx = (me_dst_idx + 1) % 4
                        if me_dst_idx == 0:
                            life_num -= 1
                            me.reset()

                #得分
                score_text = score_font.render("当前得分 : %s" % str(score), True, BLACK)
                screen.blit(score_text, (10,5))

                #显示等级信息
                level_text = level_font.render("LEVEL : %s" % str(level),True,BLACK)
                screen.blit(level_text, (10,650))

            #暂停动作
            elif paused:
                again_rect.left, again_rect.top = 150,200
                screen.blit(again_image, again_rect)

                gmov_rect.left, gmov_rect.top = 150,290
                screen.blit(gmov_image, gmov_rect)

                #检测鼠标操作
                #按下左键
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()

                    if again_rect.left < pos[0] < again_rect.right and \
                       again_rect.top < pos[1] < again_rect.bottom:
                        main()

                    elif gmov_rect.left < pos[0] < gmov_rect.right and \
                         gmov_rect.top < pos[1] < gmov_rect.bottom:
                        pygame.quit()
                        sys.exit()

            #GameOver
            elif life_num == 0:
                #BG停止
                pygame.mixer.music.stop()

                #全音效停止
                pygame.mixer.stop()

                if not recorded:
                    recorded = True
                    #读取历史最高分
                    with open("record.txt", "r") as f:
                        record_score = int(f.read())
                    #高于历史纪录，存档
                    if score > record_score:
                        with open("record.txt","w") as f:
                            f.write(str(score))

                #绘制结束界面
                record_score_text = gmov_font.render("Best: %d" % record_score,True, BLACK)
                screen.blit(record_score_text, (50, 50))

                gmov_text1 = gmov_font.render("Your Score", True, BLACK)
                gmov_text1_rect = gmov_text1.get_rect()
                gmov_text1_rect.left, gmov_text1_rect.top = \
                                      (width - gmov_text1_rect.width) // 2, gmov_text1_rect.bottom + 50
                screen.blit(gmov_text1, gmov_text1_rect)

                gmov_text2 = gmov_font.render(str(score), True, BLACK)
                gmov_text2_rect = gmov_text2.get_rect()
                gmov_text2_rect.left, gmov_text2_rect.top = \
                                      (width - gmov_text2_rect.width) // 2,\
                                      gmov_text1_rect.bottom + 10
                screen.blit(gmov_text2, gmov_text2_rect)

                again_rect.left, again_rect.top = \
                                 (width - again_rect.width) // 2,\
                                 gmov_text2_rect.bottom + 50
                screen.blit(again_image, again_rect)

                gmov_rect.left, gmov_rect.top = \
                                (width - again_rect.width) // 2,\
                                again_rect.bottom + 10
                screen.blit(gmov_image, gmov_rect)

                #检测鼠标操作
                #按下左键
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()

                    if again_rect.left < pos[0] < again_rect.right and \
                       again_rect.top < pos[1] < again_rect.bottom:
                        main()

                    elif gmov_rect.left < pos[0] < gmov_rect.right and \
                         gmov_rect.top < pos[1] < gmov_rect.bottom:
                        pygame.quit()
                        sys.exit()


            #暂停按钮
            screen.blit(paused_image, paused_rect)
        
        #切换图片
        if not(delay % 5):
            switch_image = not switch_image
            
        delay -= 1
        if not delay:
            delay = 100
        
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
