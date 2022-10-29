import pygame
from enemies.enemy import Enemy
from towers.archerMonkey import ArcherMonkeyLong, ArcherMonkeyShort
from towers.supportTower import MonkeyVillage, Alchemist
import time
import random
pygame.font.init()

lifes_img = pygame.transform.scale(pygame.image.load("game_assets/heart.png"),
                                   (40, 40))
coin_img = pygame.image.load("game_assets/coin.png")


class Game:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemies = []
        self.attack_towers = [ArcherMonkeyLong(300, 360), ArcherMonkeyShort(800, 360)]
        self.support_towers = [Alchemist(400, 360)]
        self.lives = 100
        self.money = 10
        self.bg = pygame.image.load("game_assets/game_maps/map_1.png")
        self.timer = time.time()
        self.lifes_font = pygame.font.SysFont("comicsans", 40)
        self.selected_tower = None

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            if time.time() - self.timer >= random.randrange(1, 5)/2:
                self.timer = time.time()
                self.enemies.append(random.choice([Enemy(4)]))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # checking if you clicked on attack tower
                    for tw in self.attack_towers:
                        if tw.click(pos[0], pos[1]):
                            tw.selected = True
                            self.selected_tower = tw
                        else:
                            tw.selected = False

                        # checking if you clicked on support tower
                        for tw in self.support_towers:
                            if tw.click(pos[0], pos[1]):
                                tw.selected = True
                                self.selected_tower = tw
                            else:
                                tw.selected = False

            # loop through enemies
            to_del = []
            for en in self.enemies:
                if en.x > 1300:
                    to_del.append(en)

            # delete all enemies off the screen
            for d in to_del:
                self.lives -= Enemy.attacking(d)
                self.enemies.remove(d)

            # loop through attack towers
            for atw in self.attack_towers:
                atw.attack(self.enemies)

            # loop  through support towers
            for stw in self.support_towers:
                stw.support(self.attack_towers)

            # if you lose
            if self.lives <= 0:
                print("You lost")
                run = False

            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))

        # Draw support tower
        for stw in self.support_towers:
            stw.draw(self.win)

        # Draw towers
        for atw in self.attack_towers:
            atw.draw(self.win)

        # Draw enemies
        for en in self.enemies:
            en.draw(self.win)

        # Draw lifes
        text = self.lifes_font.render(str(self.lives), 1, (0, 0, 0))
        start_x = self.width
        life = lifes_img

        self.win.blit(text, (start_x - text.get_width() - 55, 5))
        self.win.blit(life, (start_x - life.get_width() - 10, 15))

        pygame.display.update()

    def draw_menu(self):
        pass

g = Game()
g.run()