import pygame

def key_pressed():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quitting...")
            exit(1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return "LEFT"
            if event.key == pygame.K_RIGHT:
                return "RIGHT"
            if event.key == pygame.K_UP:
                return "UP"
            if event.key == pygame.K_DOWN:
                return "DOWN"
    return "NULL"

def key_pressed_wait():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("quitting...")
            exit(1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return "LEFT", True
            elif event.key == pygame.K_RIGHT:
                return "RIGHT", True
            elif event.key == pygame.K_UP:
                return "UP", True
            elif event.key == pygame.K_DOWN:
                return "DOWN", True
    return "NULL", False