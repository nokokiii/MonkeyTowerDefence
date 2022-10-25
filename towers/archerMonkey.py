import pygame
from .tower import Tower
import math
import time

tower_imgs1 = []
archer_imgs1 = []

# Load tower img
tower_imgs1.append(pygame.transform.scale(pygame.image.load("game_assets/towers/archer_long/archer_tower.png"),
                                                      (70, 70)))
# Load archer images
for x in range(1, 5):
    archer_imgs1.append(pygame.transform.scale(pygame.image.load("game_assets/towers/archer_long/long_archer_" + str(x) + ".png"),
                                                   (65, 65)))


class ArcherMonkeyLong(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs1
        self.archer_imgs = archer_imgs1
        self.archer_count = 0
        self.range = 220
        self.inRange = False
        self.left = True
        self.timer = time.time()
        self.hit_delay = 2

    def draw(self, win):
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
        win.blit(surface, (self.x - self.range, self.y - self.range))
        super().draw(win)

        if self.inRange:
            # pygame.draw.circle(surface, (255, 0, 0, 100), (self.range, self.range), self.range, 0)
            # win.blit(surface, (self.x - self.range, self.y - self.range))
            self.archer_count += 1
            if self.archer_count >= len(self.archer_imgs) * 7:
                self.archer_count = 0
        else:
            self.archer_count = 0

        archer = self.archer_imgs[self.archer_count // 7]
        win.blit(archer, ((self.x + self.width / 2) - (archer.get_width() / 2),
                          (self.y - archer.get_height() + (archer.get_height()/2) - 20)))

        # draw range circle
        circle_surface = pygame.Surface((self.range * 2, self.range * 2))
        circle_surface.set_alpha(128)

        pygame.draw.circle(circle_surface, (255, 0, 0), (self.x, self.y), self.range, 4)


    def change_range(self, r):
        """
        Change range of archer tower
        :param r: int
        :return: None
        """
        self.range = r

    def attack(self, enemies):
        """
        attacks an enemy in the enemy list, modifies the list
        :param enemies: list of enemies
        :return: None
        """
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt(((self.x - x)**2 - 16)+ (self.y - y)**2)

            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.x)
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if time.time() - self.timer >= self.hit_delay:
                self.timer = time.time()
                if first_enemy.hit() == True:
                    enemies.remove(first_enemy)

            if first_enemy.x < self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)
            elif self.left and first_enemy.x > self.x:
                self.left = False
                for x, img in enumerate(self.archer_imgs):
                    self.archer_imgs[x] = pygame.transform.flip(img, True, False)


archer_imgs2 = []
tower_imgs2 = []

# Load tower img
tower_imgs2.append(pygame.transform.scale(pygame.image.load("game_assets/towers/archer_long/archer_tower.png"),
                                                      (70, 70)))
# Load archer images
for x in range(1, 5):
    archer_imgs2.append(pygame.transform.scale(pygame.image.load("game_assets/towers/archer_short/short_archer_" + str(x) + ".png"),
                                                   (65, 65)))


class ArcherMonkeyShort(ArcherMonkeyLong):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_imgs = tower_imgs2
        self.archer_imgs = archer_imgs2
        self.archer_count = 0
        self.range = 180
        self.hit_delay = 1

