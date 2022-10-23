import pygame
from .enemy import Enemy


class One(Enemy):
    imgs = []
    img = pygame.image.load("game_assets/enemies/1/enemy_one.png")
    imgs.append(pygame.transform.scale(img, (64, 64)))

    def __init__(self):
        super().__init__()