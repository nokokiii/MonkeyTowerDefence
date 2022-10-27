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
        self.y = 250
        self.max_health = 0
        self.enemy_speed = [2.1, 2.6, 3, 3.6]
        self.speed = 0
        self.pop = False

    def draw(self, win):
        """
        Draws the enemy with the given images
        :param win: surface
        :return: None
        """
        for x in range(1, 5):
            if self.pop:
                self.img = pygame.transform.scale(pygame.image.load("game_assets/enemies/pop.png"), (70, 70))
                self.pop = False
                win.blit(self.img, (self.x, self.y))
            elif self.health == x + 1:
                self.img = self.imgs[x]
                win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, collide_x, collide_y):
        """
        Returns if position has hit enemy
        :param collide_x: int
        :param collide_y: int
        :return: Bool
        """
        if collide_x <= self.x + self.width and collide_x >= self.x:
            if collide_y <= self.y + self.height and collide_y >= self.y:
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: None
        """
        for x in range(4):
            if self.health == x:
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
