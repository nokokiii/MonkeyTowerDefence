import pygame
from .tower import Tower
import math

monkey_village_imgs = [
    pygame.transform.scale(pygame.image.load("game_assets/towers/support_tower/monkey_village.png"), (86, 86))]


class MonkeyVillage(Tower):
    """
    Adding more range to towers in its range
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 75
        self.tower_imgs = monkey_village_imgs[:]
        self.effect = [1, 2]

    def draw(self, win):
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
        win.blit(surface, (self.x - self.range, self.y - self.range))
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
            tower.range += round(tower.range * self.effect[self.level - 1])


alchemist_imgs = [pygame.transform.scale(pygame.image.load("game_assets/towers/support_tower/alchemist.png"), (80, 80))]


class Alchemist(MonkeyVillage):
    """
    Adding more damage to towers in its range
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 100
        self.effect = [1, 2]
        self.tower_imgs = alchemist_imgs[:]

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
            tower.damage += round(tower.damage * self.effect[self.level - 1])
