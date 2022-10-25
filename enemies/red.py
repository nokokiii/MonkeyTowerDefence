import pygame
from .enemy import Enemy

imgs = []
img = pygame.image.load("game_assets/enemies/enemy_1.png")
imgs.append(pygame.transform.scale(img, (55, 55)))


class Red(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = []
        self.max_health = 1
        self.health = self.max_health
        self.enemy_speed = 1.9