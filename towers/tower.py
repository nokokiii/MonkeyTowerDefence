import pygame


class Tower:
    """
    Abstract class for towers
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_price = [0, 0, 0]
        self.price = [0, 0, 0]
        self.level = 1
        self.selected = False
        self.menu = None
        self.original_range = 0
        self.range = 0
        self.tower_imgs = []
        self.damage = 0

    def draw(self, win):
        """
        draws the tower
        :param win: surface
        :return: None
        """
        img = self.tower_imgs[self.level - 1]
        win.blit(img, (self.x - img.get_width() // 2, self.y - img.get_height() // 2))

        # draw menu
        if self.selected:
            self.menu.draw(win)

    def draw_radius(self, win):
        # if self.selected:
        #     # draw range circle
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

        win.blit(surface, (self.x - self.range, self.y - self.range))

    def click(self, X, Y):
        """
        Returns True if tower has been clicked on
        and selects tower id it was clicked
        :param X: int
        :param Y: int
        :return: Bool
        """
        img = self.tower_imgs[self.level - 1]
        if self.x - img.get_width() // 2 + self.width >= X >= self.x - img.get_width() // 2:
            if self.y + self.height - img.get_height() // 2 >= Y >= self.y - img.get_height() // 2:
                return True
        return False

    def sell(self):
        """
        Call to sell the tower, returns sell price
        :return: int
        """
        return self.sell_price[self.level-1]

    def upgrade(self):
        """
        Upgrades the tower for a given cost
        :return: None
        """
        self.level += 1
        self.damage += 1

    def get_upgrade_cost(self):
        """
        Returns the upgrade cost, if 0 then can't upgrade
        anymore
        :return: int
        """
        return self.price[self.level - 1]

    def move(self, x, y):
        self.x = x
        self.y = y
