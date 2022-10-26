import pygame
import math


class Enemy:
    def __init__(self):
        self.width = 64
        self.height = 64
        self.health = 1
        self.path = [-100, 1300]
        self.x = self.path[0]
        self.y = 250
        self.img = None
        self.max_health = 0
        self.enemy_speed = [1.9, 2.2, 2.7, 3.5]
        self.speed = 0
        self.pop = False

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        for x in range(4):
            if self.pop:
                pop_img = pygame.transform.scale(pygame.image.load("game_assets/enemies/pop.png"), (70, 70))
                self.img = pop_img
                self.pop = False
            elif self.health == x + 1:
                self.img = self.imgs[x]
        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        """
        Returns if position has hit enemy
        :param X: int
        :param Y: int
        :return: Bool
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: None
        """
        x1 = self.path[0]
        x2 = self.path[1]

        for x in range(4):
            if self.health == x:
                self.speed = self.enemy_speed[x]

        move_x = (self.x + self.speed)
        self.x = move_x

    def hit(self):
        """
        Return if an enemy has dies and removes one health
        each call
        :return: Bool
        """
        self.pop = True
        self.health -= 1
        if self.health <= 0:
            return True
        return False
