import pygame
from .enemy import Enemy


class Blue(Enemy):

    def __init__(self):
        super().__init__()
        self.imgs = []
        self.max_health = 2
        self.health = self.max_health

        for x in range(2):
            add_str = str(x+1)
            img = pygame.image.load("game_assets/enemies/enemy_" + add_str + ".png")
            self.imgs.append(pygame.transform.scale(img, (55, 55)))


