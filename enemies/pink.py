import pygame
from .enemy import Enemy

imgs = []
img = pygame.image.load("game_assets/enemies/enemy_4.png")
imgs.append(pygame.transform.scale(img, (62, 62)))

class Pink(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = imgs
        self.max_health = 4
        self.health = self.max_health
        self.enemy_speed = 4


