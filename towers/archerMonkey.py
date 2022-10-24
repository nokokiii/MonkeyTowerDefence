import pygame
from .tower import Tower
import math


class ArcherMonkeyLong(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0
        self.range = 220
        self.inRange = False

        self.tower_imgs.append(pygame.transform.scale(pygame.image.load("game_assets/towers/archer_long/archer_tower.png"),
                                                      (70, 70)))

        # Load archer images
        for x in range(1, 5):
            self.archer_imgs.append(pygame.transform.scale(pygame.image.load("game_assets/towers/archer_long/long_archer_" + str(x) + ".png"),
                                                           (55, 55)))

    def draw(self, win):
        super().draw(win)
        if self.inRange:
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 7:
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count // 7]
        win.blit(archer, ((self.x + self.width / 2) - (archer.get_width() / 2),
                          (self.y - archer.get_height() + (archer.get_height() / 2) - 5)))

    def change_range(self, r):
        """
        Change range of archer tower
        :param r: int
        :return: None
        """
        self.range = r

    def attack(self, enemies):
        """
        Attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """
        self.inRange = False
        closest_enemy = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)

            if dis < self.range:
                self.inRange = True
                closest_enemy.append(enemy)




