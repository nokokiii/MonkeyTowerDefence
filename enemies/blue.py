import pygame
from .enemy import Enemy

imgs = []
img = pygame.image.load("game_assets/enemies/enemy_2.png")
imgs.append(pygame.transform.scale(img, (57, 57)))

class Blue(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = imgs
        self.max_health = 2
        self.health = self.max_health
        self.enemy_speed = 2.2



