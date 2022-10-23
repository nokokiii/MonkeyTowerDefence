import pygame
from monkey_tower import Tower

class ArcherMonkeyLong():
    def __init__(self, x, y):
        super().__init__(self, x, y)
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = []

        # Load archer tower images
        for x in range(1,4):
            self.tower_imgs.append(pygame.transform.scale(pygame.image.load("game_asstes/towers/archer_long_" + str(x) + ".png"), (70, 70)))

        for x in range(1,4):
            self.tower_imgs.append(pygame.transform.scale(pygame.image.load("game_asstes/towers/archer_short_" + str(x) + ".png"), (70, 70)))
    def draw(self, win):
        super().draw(win)

    def attack(self, enemies):
        """
        Attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """