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
        self.imgs = []

    def draw(self, win):
        pass

    def draw(self):
        pass

    def click(self):
        pass

    def sell(self):
        pass

    def upgrade(self):
        pass

    def move(self):
        pass