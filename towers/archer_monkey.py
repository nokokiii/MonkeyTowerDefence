import pygame
from .monkey_tower import Tower


class ArcherMonkeyLong(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = pygame.transform.scale(pygame.image.load("game_assets/towers/archer_long/archer_tower.png"), (70, 70))
        self.archer_imgs = []
        self.archer_count = 0

        # Load archer images
        for x in range(1, 5):
            self
    def draw(self, win):
        super().draw(win)
        tower = self.tower_imgs[0]
        win.blit(tower, ((self.x + self.width/2) - (tower.get_width()/2)), (self.y - (tower.get_height()/2)))

        self.archer_count += 1

    def attack(self, enemies):
        """
        Attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """