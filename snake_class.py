import pygame


class SnakeBlock(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()


        self.rect = self.img.get_rect()
        self.rect.center = pos

    def move_right(self, movement):
        self.rect.x += movement

    def move_left(self, movement):
        self.rect.x -= movement

    def move_up(self, movement):
        self.rect.y -= movement

    def move_down(self, movement):
        self.rect.y += movement

    def enemy_left(self):
        self.rect.x -=1


class User(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos