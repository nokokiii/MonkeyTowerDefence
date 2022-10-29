import pygame
from .tower import Tower
import math

monkey_village_imgs = [
    pygame.transform.scale(pygame.image.load("game_assets/towers/support_tower/monkey_village.png"), (85, 85))]


class MonkeyVillage(Tower):
    """
    Adding more range to towers in its range
    """
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 90
        self.tower_imgs = monkey_village_imgs[:]
        self.width = self.height = 85
        self.effect = [0.2, 0.4]

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)

    def support(self, towers):
        """
        Will modify towers according to ability
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt(((self.x - x) ** 2 - 16) + (self.y - y) ** 2)

            if dis <= self.range:
                effected.append(tower)
        for tower in effected:
            tower.range = tower.original_range + round(tower.original_range * self.effect[self.level - 1])


alchemist_imgs = [pygame.transform.scale(pygame.image.load("game_assets/towers/support_tower/alchemist.png"), (80, 80))]


class Alchemist(MonkeyVillage):
    """
    Adding more damage to towers in its range
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.effect = [2, 3]
        self.tower_imgs = alchemist_imgs[:]
        self.width = self.height = 80

    def support(self, towers):
        """
        Will modify towers according to ability
        :param towers: list
        :return: None
        """
        effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt(((self.x - x) ** 2 - 16) + (self.y - y) ** 2)

            if dis <= self.range:
                effected.append(tower)
        for tower in effected:
            tower.damage = round(tower.original_damage * self.effect[self.level - 1])
