import pygame
from .enemy import Enemy

imgs = []
img = pygame.image.load("game_assets/enemies/enemy_3.png")
imgs.append(pygame.transform.scale(img, (60, 60)))


class Green(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = imgs
        self.max_health = 3
        self.health = self.max_health
        self.enemy_speed = 2.5


