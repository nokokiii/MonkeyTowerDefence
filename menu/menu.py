import pygame


class Menu:
    """
    Menu for holdiong items
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.items_names = []
        self.imgs = []
        self.items = 0