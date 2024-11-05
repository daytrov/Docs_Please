import pygame
import sys
from buttons import imageButton


WIDTH = 1820
HEIGHT = 980
FPS = 60


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DOCS PLEASE')
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

start_button = imageButton(WIDTH/2-(252/2), 600, 252, 78, "", "C:\\Users\сметана\\Documents\\GitHub\\Docs_Please\images\\Start-game.png", "C:\\Users\сметана\\Documents\\GitHub\\Docs_Please\images\\Start-game-hover.png", "C:\\Users\сметана\\Documents\\GitHub\\Docs_Please\sound\startbut-sound.mp3")
settings_button = imageButton(WIDTH/2-(252/2), 700, 252, 78, "", "C:\\Users\сметана\\Documents\\GitHub\\Docs_Please\images\\Settings-button.png", "C:\\Users\сметана\\Documents\\GitHub\\Docs_Please\images\\Settings-button-hover.png", "C:\\Users\сметана\\Documents\\GitHub\\Docs_Please\sound\startbut-sound.mp3")
logo_image = pygame.image.load('C:\\Users\сметана\\Documents\\GitHub\\Docs_Please\images\logo.png').convert_alpha()
background_image = pygame.image.load('C:\\Users\сметана\\Documents\\GitHub\\Docs_Please\images\Background-img.jpg').convert_alpha()
background_image = pygame.transform.scale(background_image, (1820, 980))
back_button = imageButton(WIDTH/2-(252/2), 600, 252, 78, "", "C:\\Users\сметана\\Documents\\GitHub\\Docs_Please\images\\Back-button.png", "C:\\Users\сметана\\Documents\\GitHub\\Docs_Please\images\\Back-button-hover.png", "C:\\Users\сметана\\Documents\\GitHub\\Docs_Please\sound\startbut-sound.mp3")


def start_menu ():
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == settings_button:
                fade()
                settings_menu()
            if event.type == pygame.USEREVENT and event.button == start_button:
                fade()
                game_screen()
            for btn in [start_button, settings_button]:
                btn.handle_event(event)
        screen.blit(logo_image, (0, 100))
        for btn in [start_button, settings_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen) 
        pygame.display.flip()


def settings_menu ():
    running = True
    while running:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    fade()
            if event.type == pygame.USEREVENT and event.button == back_button:
                running = False
                fade()
            for btn in [back_button]:
                btn.handle_event(event)
        for btn in [back_button]:
            btn.check_hover(pygame.mouse.get_pos())
            btn.draw(screen) 
        pygame.display.update()


def game_screen ():
    running = True
    while running:
        screen.blit(background_image, (0,0))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings_menu()


def fade ():
    running = True
    fade_alpha = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill((0,0,0))
        fade_surface.set_alpha(fade_alpha)
        screen.blit(fade_surface, (0, 0))
        fade_alpha += 5
        if fade_alpha >= 105:
            fade_alpha = 255
            running = False
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    start_menu()