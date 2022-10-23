import pygame
from .enemy import Enemy


class Green(Enemy):
    imgs = []
    img = pygame.image.load("game_assets/enemies/3/enemy_green.png")
    imgs.append(pygame.transform.scale(img, (60, 60)))

    def __init__(self):
        super().__init__()