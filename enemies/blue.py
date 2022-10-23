import pygame
from .enemy import Enemy


class Blue(Enemy):
    imgs = []
    img = pygame.image.load("game_assets/enemies/2/enemy_blue.png")
    imgs.append(pygame.transform.scale(img, (64, 64)))

    def __init__(self):
        super().__init__()