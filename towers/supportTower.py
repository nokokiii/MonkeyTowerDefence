import pygame
from .tower import Tower
import math
import time

support_monkeys_imgs = [pygame.transform.scale(pygame.image.load("game_assets/tower/support_tower/monkey_village.png"), (70, 70)),
                   pygame.transform.scale(pygame.image.load("game_assets/tower/support_tower/alchemist.png"), (70, 70))]


class MonkeyVillage(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 150
        self.imgs = support_monkeys_imgs[0]

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)


class Alchemist(MonkeyVillage):
    def __init__(self):
        pass


