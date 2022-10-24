import pygame
from .enemy import Enemy


class Pink(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = []
        self.health_imgs = []
        self.max_health = 4
        self.health = self.max_health

        img = pygame.image.load("game_assets/enemies/enemy_4.png")
        self.imgs.append(pygame.transform.scale(img, (55, 55)))

