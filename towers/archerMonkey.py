import pygame
from .tower import Tower


class ArcherMonkeyLong(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = []
        self.archer_imgs = []
        self.archer_count = 0

        self.tower_imgs.append(pygame.transform.scale(pygame.image.load("game_assets/towers/archer_long/archer_tower.png"), (70, 70)))

        # Load archer images
        for x in range(1, 5):
            self.archer_imgs.append(pygame.transform.scale(pygame.image.load("game_assets/towers/archer_long/long_archer_" + str(x) + ".png"), (70, 70)))

    def draw(self, win):
        super().draw(win)
        if self.archer_count >= len(self.archer_imgs):
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count]
        win.blit(archer, ((self.x + self.width/2) - (archer.get_width()/2), (self.y - archer.get_height())))

        self.archer_count += 1

    def attack(self, enemies):
        """
        Attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """
        pass