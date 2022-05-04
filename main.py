import sys
import pygame
import time

clock = pygame.time.Clock()
dmgPerSecond = 0
dmgPerClick = 1
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
light_grey = (224, 224, 224)
light_blue = (173, 216, 230)
grey = (128, 128, 128)
blue = (0, 100, 250)

sprites = [1]
sprites[0] = pygame.image.load('images/test.png')

pygame.init()
screen = pygame.display.set_mode((1200, 800))
bg_color = blue
pygame.display.set_caption("Clicker v0.1")


class Enemy1:
    def __init__(self, screen, hp=200, i=0):
        self.screen = screen
        self.image = sprites[0]
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
# Parameters of HP bar
        self.hp_current = hp
        self.hp_max = hp
        self.hp_bar_len = 600
        self.hp_ratio = self.hp_max / self.hp_bar_len

    def spawn(self):
        self.screen.blit(self.image, self.rect)

    def get_dmg(self, dmg):
        if self.hp_current > 0:
            self.hp_current -= dmg
        if self.hp_current <= 0:
            self.hp_current = 0

    def hp_bar(self):
        # hp_surface = pygame.Surface(self.hp_current/self.hp_ratio, 25)
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, self.hp_current/self.hp_ratio, 40))
        pygame.draw.rect(screen, (255, 255, 255), (10, 10, self.hp_bar_len, 40), 4)

    def update(self):
        self.hp_bar()


def draw_text(text, textcolor, rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, textcolor, rectcolor)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)


def run_game():
    lvl = 1
    enemy_1 = Enemy1(screen)
    while True:
        screen.fill(bg_color)
        enemy_1.spawn()
        draw_text("Poziom: "+str(lvl), black, blue, 400, 100, 50)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                global dmgPerClick
                dmgPerClick = dmgPerClick + 1
                print(enemy_1.hp_current)
                enemy_1.get_dmg(dmgPerClick)
            if event.type == pygame.QUIT:
                sys.exit()

        enemy_1.hp_bar()
        pygame.display.flip()
        clock.tick(60)


run_game()
