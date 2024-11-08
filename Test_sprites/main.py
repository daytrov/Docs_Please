import pygame
import sys
import os


WIDTH = 1820
HEIGHT = 980
FPS = 60

os.chdir(os.path.dirname(os.path.dirname(__file__)))

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DOCS PLEASE')
clock = pygame.time.Clock()


background_image = pygame.image.load('images\\Background-img.jpg').convert_alpha()
background_image = pygame.transform.scale(background_image, (1820, 980))


class Character(pygame.sprite.Sprite):
    def __init__(self, x, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 500))
        self.is_hovered = False
    def update(self):
        if self.rect.x < WIDTH/2-180:
            self.rect.x += 3
        else:
            self.rect.x = WIDTH/2-180 
    

class imageButton:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path = None, sound_path = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)
        self.is_hovered = False

    def draw(self, screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)

        # font = pygame.font.Font(None, 40)
        # text_surface = font.render(self.text, True, (255,255,255))
        # text_rect = text_surface.get_rect(center = self.rect.center)
        # screen.blit(text_surface, text_rect)
    
    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


all_sprites = pygame.sprite.Group()
person = Character(-200, 'images\\person.png')
computer = imageButton(1000, 500, 350, 350, '','images\\комп.png', 'images\\комп-hover.png','')
table = imageButton(300, 500, 1400, 1000, '', 'images\\Table-PNG-Photos.png', '', '')
documents = imageButton(500, 500, 300, 300, '', 'images\\доки спрайт.png', '','')
all_sprites.add(person)
form = imageButton(500,200, 650, 650, "", 'images\\form_comp.jpg','', '')



def game_screen ():
    running = True
    index = -1
    while running:
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        clock.tick(FPS)

        table.draw(screen)
        person.update()
        
        for interaction_items in [table, computer, documents]:
            interaction_items.draw(screen)
            interaction_items.check_hover(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if table.rect.collidepoint(event.pos):
                        index += 1

        if index % 2 == 0:
            form.draw(screen)

        pygame.display.update()

if __name__ == "__main__":
    game_screen()