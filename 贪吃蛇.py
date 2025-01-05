#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:55:13 2024

@author: baowenhan
"""

import pygame
import time
import random
import sys

# 初始化pygame
pygame.init()

# 设置屏幕尺寸
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("贪吃蛇小游戏")

# 颜色定义
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue=(0,0,255)

# 蛇的初始设置
snake_block = 10

font_style = pygame.font.SysFont("bahnschrift", 25)

def your_score(score):
    value = font_style.render("score: " + str(score), True, white)
    screen.blit(value, [0, 0])
    
def your_speed(speed):
    value=font_style.render("speed: "+str(speed),True,white)
    screen.blit(value,[0,20])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1
    snake_speed=1

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
    
    badfoodx=round(random.randrange(0,screen_width-snake_block)/10.0)*10.0
    badfoody=round(random.randrange(0,screen_height-snake_block)/10.0)*10.0
    
    poisonx=round(random.randrange(0,screen_width-snake_block)/10.0)*10.0
    poisony=round(random.randrange(0,screen_height-snake_block)/10.0)*10.0

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("You failed! Press Q to exit or C to continue.", red)
            your_score(Length_of_snake - 1)
            your_speed(Length_of_snake)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if Length_of_snake>5:
            pygame.draw.rect(screen, white, [badfoodx,badfoody,snake_block,snake_block])
        if Length_of_snake>10:
            pygame.draw.rect(screen, blue, [poisonx,poisony,snake_block,snake_block])
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(Length_of_snake - 1)
        your_speed(Length_of_snake)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_speed+=1
            if snake_speed>25:
                snake_speed=25
        if x1==badfoodx and y1==badfoody:
            badfoodx=round(random.randrange(0,screen_width-snake_block)/10.0)*10.0
            badfoody=round(random.randrange(0,screen_height-snake_block)/10.0)*10.0
            Length_of_snake-=1
            if Length_of_snake<1:
                game_close=True
        if x1==poisonx and y1==poisony:
            poisonx=round(random.randrange(0,screen_width-snake_block)/10.0)*10.0
            poisony=round(random.randrange(0,screen_height-snake_block)/10.0)*10.0
            game_close=True
            
        clock.tick(snake_speed)

    pygame.quit()
    quit()

clock = pygame.time.Clock()
gameLoop()