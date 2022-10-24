import pygame
from .enemy import Enemy


class Green(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = []
        self.max_health = 3
        self.health = self.max_health

        img = pygame.image.load("game_assets/enemies/3/enemy_green.png")
        self.imgs.append(pygame.transform.scale(img, (60, 60)))
