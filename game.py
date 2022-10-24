import pygame
from enemies.red import Red
from enemies.blue import Blue
from enemies.green import Green
from enemies.pink import Pink
from towers.archerMonkey import ArcherMonkeyLong


class Game:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = [Pink()]
        self.towers = [ArcherMonkeyLong(300,360)]
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

            # loop through enemies b
            to_del = []
            for en in self.enemies:
                if en.x > 1300:
                    to_del.append(en)

            # delete all enemies off the screen
            for d in to_del:
                self.enemies.remove(d)

            # loop through towers
            for tw in self.towers:
                tw.attack(self.enemies)
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