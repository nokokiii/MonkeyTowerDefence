import pygame
import math


class Enemy:
    imgs = []

    def __init__(self):
        self.width = 64
        self.height = 64
        self.health = 1
        self.path = [-100, 1300]
        self.x = self.path[0]
        self.y = 225
        self.img = None
        self.max_health = 0

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        self.img = self.imgs[0]
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

        dirn = (x2-x1)/500

        move_x = (self.x + dirn)
        self.x = move_x

    def hit(self):
        """
        Return if an enemy has dies and removes one health
        each call
        :return: Bool
        """
        self.health -= 1
        if self.health <= 0:
            return True