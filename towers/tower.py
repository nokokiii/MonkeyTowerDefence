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
        self.range = 0
        self.tower_imgs = []
        self.damage = 0

    def draw(self, win):
        """
        Draws the tower
        :param win: surface
        :return: None
        """
        img = self.tower_imgs[self.level - 1]
        win.blit(img, (self.x - img.get_width()//2, self.y - img.get_height()//2))

    def draw_radius(self, win):
        # draw range circle
        circle_surface = pygame.Surface((self.range * 2, self.range * 2))
        circle_surface.set_alpha(128)

        pygame.draw.circle(circle_surface, (255, 0, 0), (self.x, self.y), self.range, 4)

    def click(self, X, Y):
        """
        Returns if tower has been clicked on
        and selects tower id it was clicked
        :param X: int
        :param Y: int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
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
