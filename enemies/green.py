import pygame
from .enemy import Enemy

imgs = []
for x in range(1, 4):
    add_str = str(x+1)
    img = pygame.image.load("game_assets/enemies/enemy_" + add_str + ".png")
    imgs.append(pygame.transform.scale(img, (60, 60)))


class Green(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = imgs
        self.max_health = 3
        self.health = self.max_health



