import pygame
from .enemy import Enemy

imgs = []
for x in range(1, 3):
    add_str = str(x)
    img = pygame.image.load("game_assets/enemies/enemy_" + add_str + ".png")
    imgs.append(pygame.transform.scale(img, (60, 60)))


class Blue(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = imgs
        self.max_health = 2
        self.health = self.max_health




