import pygame
from .tower import Tower
import math
import time


monkey_village_imgs = [pygame.transform.scale(pygame.image.load("game_assets/towers/support_tower/monkey_village.png"), (70, 70))]


class MonkeyVillage(Tower):
    """
    Adding more range to towers in its range
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 75
        self.tower_imgs = monkey_village_imgs[:]
        self.effect = [1 ,2]

    def draw(self, win):
        super().draw(win)
        super().draw_radius(win)

    def support(self, towers):
        """
        Will modify towers according to ability
        :param towers: list
        :return: None
        """
        pass

alch_imgs = [pygame.transform.scale(pygame.image.load("game_assets/towers/support_tower/alchemist.png"), (70, 70))]

class Alchemist(MonkeyVillage):
    """
    Adding more damage to towers in its range
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.effect = [1, 2]
        self.tower_imgs = alch_imgs[:]

    def support(self, towers):
        """
        Will modify towers according to ability
        :param towers: list
        :return: None
        """
        pass