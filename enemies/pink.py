import pygame
from .enemy import Enemy


class Pink(Enemy):

    def __init__(self):
        super().__init__()
        self.health_imgs = []
        self.max_health = 4
        self.health = self.max_health

        for x in range(4):
            add_str = str(4 - x)
            img = pygame.image.load("game_assets/enemies/enemy_" + add_str + ".png")
            self.health_imgs.append(pygame.transform.scale(img, (55, 55)))