import pygame
from enemies.red import Red
from enemies.blue import Blue
from enemies.green import Green
from enemies.pink import Pink
from towers.archer_monkey import ArcherMonkeyLong


class Game:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Pink(), Green(), Blue(), Red()]
        self.towers = [ArcherMonkeyLong(100, 100)]
        self.lives = 10
        self.money = 10
        self.bg = pygame.image.load("game_assets/game_maps/map_1.png")

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        # draw enemies
        for en in self.enemies:
            en.draw(self.win)

        # draw towers
        for tw in self.towers:
            tw.draw(self.win)
        pygame.display.update()

g = Game()
g.run()