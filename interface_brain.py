import time

import pygame



def draw_snake(byte_list, last_x, last_y, screen, x_pos_food, y_pos_food, add_block):
    eaten = False
    temp_x = last_x
    temp_y = last_y
    times = 0
    pos_list_x = []
    pos_list_y = []
    if add_block:
        print("01test success")
        #time.sleep(1)
        number = len(byte_list)
        number = number - 1
        last_byte = byte_list[0]
        last_byte_1 = str(last_byte)
        byte_list.append(last_byte_1[0])

    for byte in byte_list:
        if times == 0:
            temp_byte_list = []
            '''if times == 1:
                temp_byte_list.append(byte)'''
        else:
            '''if add_block:
                if times == 1:
                    temp_byte_list.append(byte)'''
            temp_byte_list.append(byte)
        times = times + 1

        if byte == 'RIGHT':
            temp_x = temp_x + 20
            if temp_x > 350:
                temp_x = 5
        elif byte == 'LEFT':
            temp_x = temp_x - 20
            if temp_x < 0:
                temp_x = 345
        elif byte == 'UP':
            temp_y = temp_y - 20
            if temp_y < 0:
                temp_y = 345
        elif byte == 'DOWN':
            temp_y = temp_y + 20
            if temp_y > 350:
                temp_y = 5

        if times == 1:
            last_x = temp_x
            last_y = temp_y
        pos_list_x.append(temp_x)
        pos_list_y.append(temp_y)
        pygame.draw.rect(screen, (150, 30, 90), (temp_x, temp_y, 19, 19))
    byte_list.clear()
    if times > 1:
        for byte in temp_byte_list:
            byte_list.append(byte)
    if temp_x == x_pos_food:
        if temp_y == y_pos_food:
            eaten = True
    head_x = temp_x
    head_y = temp_y
    return byte_list, last_x, last_y, pos_list_x, pos_list_y, eaten, head_x, head_y


def collision_detection(head_x, head_y, pos_list_x, pos_list_y):
    cycle = 0
    for x in pos_list_x:
        head = len(pos_list_x)
        if head > 3:
            head -= 1
            print(head)
            # 1pos_list_x = []
            pos_list_x.pop(head)
            print(x)
            pos_list_x
            if head_x == x:
                print(x)
                print(pos_list_x)
                print("whaaaatt")
                if head_y == pos_list_y[cycle]:
                    exit(56)

            cycle += 1
