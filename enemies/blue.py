import pygame
from .enemy import Enemy


class Blue(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = []
        self.max_health = 2
        self.health = self.max_health

        img = pygame.image.load("game_assets/enemies/2/enemy_blue.png")
        self.imgs.append(pygame.transform.scale(img, (55, 55)))