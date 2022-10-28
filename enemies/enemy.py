import pygame

# Loading balloons images
imgs = []
for x in range(1, 5):
    add_str = str(x)
    print()
    img = pygame.image.load("game_assets/enemies/enemy_" + add_str + ".png")
    imgs.append(pygame.transform.scale(img, (60, 60)))


class Enemy:
    def __init__(self, max_health):
        self.imgs = imgs
        self.img = None
        self.width = 64
        self.height = 64
        self.path = [-100, 1300]
        self.x = self.path[0]
        self.y = 250
        self.max_health = max_health
        self.health = self.max_health
        self.enemy_speed = [2.1, 2.6, 3, 3.6]
        self.speed = 0
        self.pop = False

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        for z in range(4):
            if self.pop:
                self.img = pygame.transform.scale(pygame.image.load("game_assets/enemies/pop.png"),
                                                  (70, 70))
                self.pop = False
                win.blit(self.img, (self.x, self.y))
            elif self.health == z + 1:
                self.img = self.imgs[z]
                win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, collide_x, collide_y):
        """
        Returns if position has hit enemy
        :param collide_x: int
        :param collide_y: int
        :return: Bool
        """
        if self.x + self.width >= collide_x >= self.x:
            if self.y + self.height >= collide_y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: None
        """
        for x in range(4):
            if self.health == x + 1:
                self.speed = self.enemy_speed[x]

        move_x = (self.x + self.speed)
        self.x = move_x

    def hit(self, damage):
        """
        Return if an enemy has dies and removes one health
        each call
        :return: Bool
        """
        self.pop = True
        self.health -= damage
        if self.health <= 0:
            return True
        return False

    def attacking(self):
        return self.health
