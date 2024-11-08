import pygame
import sys
from sprites import Table
from sprites import Character
from main import settings_menu

WIDTH = 1820
HEIGHT = 980
FPS = 60


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DOCS PLEASE')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

background_image = pygame.image.load('..\\images\\Background-img.jpg').convert_alpha()
background_image = pygame.transform.scale(background_image, (1820, 980))
Employer = Character(3,'..\\images\\person.png')
Table = Table('..\\images\\Table-PNG-Photos.png')

all_sprites.add(Table, Employer)

def game_screen ():
    running = True
    while running:
        screen.blit(background_image, (0,0))
        screen.blit(Table.image, Table.rect)
        pygame.display.update()
        clock.tick(FPS)

        Employer.update()
        Table.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings_menu()