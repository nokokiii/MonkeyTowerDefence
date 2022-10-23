import pygame
from .enemy import Enemy


class Pink(Enemy):
    imgs = []
    img = pygame.image.load("game_assets/enemies/4/enemy_pink.png")
    imgs.append(pygame.transform.scale(img, (64, 64)))

    def __init__(self):
        super().__init__()