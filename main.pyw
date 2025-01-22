import time
import input
import pygame as pg

import food_brain
from snake_class import SnakeBlock
import interface_brain






fp_reg = 10
add_block = False
byte_list = []#, 'UP', 'UP', 'UP', 'UP','UP']
fps = pg.time.Clock()
inputted = False

#pg.display.flip()


def game_init():

    global dir, inputted, old_dir, byte_list, last_x, last_y, screen, x_pos_food, y_pos_food, add_block

    last_x = 165
    last_y = 165

    pg.init()
    screen = pg.display.set_mode((368, 368))
    pg.draw.rect(screen, (150, 30, 90), (170, 170, 19, 19))
    x_pos_food, y_pos_food = food_brain.print_food(screen, [5], [5])
    pg.display.flip()

    while not inputted:
        dir, inputted = input.key_pressed_wait()
    old_dir = dir
    byte_list.append(dir)
    interface_brain.draw_snake(byte_list, last_x, last_y, screen, x_pos_food, y_pos_food, add_block)

game_init()

while True:
    fps.tick(fp_reg)
    #time.sleep(0.5)
    dir = input.key_pressed()
    if dir != old_dir:
        if dir == 'RIGHT':
            if old_dir == 'LEFT':
                dir = input.key_pressed()
        if dir == 'LEFT':
            if old_dir == 'RIGHT':
                dir = input.key_pressed()
        if dir == 'UP':
            if old_dir == 'DOWN':
                dir = input.key_pressed()
        if dir == 'DOWN':
            if old_dir == 'UP':
                dir = input.key_pressed()
    if dir == 'NULL':
        byte_list.append(old_dir)
    else:
        old_dir = dir
        byte_list.append(dir)
    screen.fill((0, 0, 0))
    byte_list, last_x, last_y, pos_list_x, pos_list_y, eaten, head_x, head_y = interface_brain.draw_snake(byte_list, last_x, last_y, screen, x_pos_food, y_pos_food, add_block)
    interface_brain.collision_detection(head_x, head_y, pos_list_x, pos_list_y)
    if eaten:
        x_pos_food, y_pos_food = food_brain.print_food(screen, pos_list_x, pos_list_y)
        add_block = True
    else:
        food_brain.print_food_(screen, x_pos_food, y_pos_food)
        add_block = False
    pg.display.flip()
