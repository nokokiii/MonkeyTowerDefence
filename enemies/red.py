import pygame
from .enemy import Enemy


class Red(Enemy):
    imgs = []
    img = pygame.image.load("game_assets/enemies/1/enemy_red.png")
    imgs.append(pygame.transform.scale(img, (50, 50)))

    def __init__(self):
        super().__init__()