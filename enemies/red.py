import pygame
from .enemy import Enemy


class Red(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = []
        self.max_health = 1
        self.health = self.max_health

        img = pygame.image.load("game_assets/enemies/enemy_1.png")
        self.imgs.append(pygame.transform.scale(img, (50, 50)))