import random
import time

import pygame

def print_food_(screen, x, y):
    pygame.draw.rect(screen, (50, 130, 90), (x, y, 19, 19))


def print_food(screen, pos_list_x, pos_list_y):
    x_pos, y_pos = ran_food_pos(pos_list_x, pos_list_y)
    pygame.draw.rect(screen, (50, 130, 90), (x_pos, y_pos, 19, 19))
    return x_pos, y_pos

def pos_check(pos_list_x, pos_list_y, x_choice, y_choice):
    pos = 0
    for x in pos_list_x:
        if x == x_choice:
            print("error 01")
            if y_choice == pos_list_y[pos]:
                    print ("critical error")
                    print(x_choice)
                    print(y_choice)
                    print("error report")
                    print(pos_list_x)
                    print(pos_list_y)
                    #time.sleep(2)
                    return True
        pos += 1
    return False


def convert_x(x_choice):
    if x_choice == 1:
        x = 5
    elif x_choice == 2:
        x = 25
    elif x_choice == 3:
        x = 45
    elif x_choice == 4:
        x = 65
    elif x_choice == 5:
        x = 85
    elif x_choice == 6:
        x = 105
    elif x_choice == 7:
        x = 125
    elif x_choice == 8:
        x = 145
    elif x_choice == 9:
        x = 165
    elif x_choice == 10:
        x = 185
    elif x_choice == 11:
        x = 205
    elif x_choice == 12:
        x = 225
    elif x_choice == 13:
        x = 245
    elif x_choice == 14:
        x = 265
    elif x_choice == 15:
        x = 285
    elif x_choice == 16:
        x = 305
    elif x_choice == 17:
        x = 325
    elif x_choice == 18:
        x = 345
    return x


def convert_y(y_choice):
    if y_choice == 1:
        y = 5
    elif y_choice == 2:
        y = 25
    elif y_choice == 3:
        y = 45
    elif y_choice == 4:
        y = 65
    elif y_choice == 5:
        y = 85
    elif y_choice == 6:
        y = 105
    elif y_choice == 7:
        y = 125
    elif y_choice == 8:
        y = 145
    elif y_choice == 9:
        y = 165
    elif y_choice == 10:
        y = 185
    elif y_choice == 11:
        y = 205
    elif y_choice == 12:
        y = 225
    elif y_choice == 13:
        y = 245
    elif y_choice == 14:
        y = 265
    elif y_choice == 15:
        y = 285
    elif y_choice == 16:
        y = 305
    elif y_choice == 17:
        y = 325
    elif y_choice == 18:
        y = 345

    return y


def ran_food_pos(pos_list_x, pos_list_y):
    exists = True
    while exists:
        x_choice = random.randint(1, 18)
        y_choice = random.randint(1, 18)
        x_choice = convert_x(x_choice)
        y_choice = convert_y(y_choice)
        while exists:
            print("test success")
            #time.sleep(1)
            exists = pos_check(pos_list_x, pos_list_y, x_choice, y_choice)
            if exists:
                x_choice = random.randint(1, 18)
                y_choice = random.randint(1, 18)
                x_choice = convert_x(x_choice)
                y_choice = convert_y(y_choice)
        print(x_choice)
        print(y_choice)
        return x_choice, y_choice

