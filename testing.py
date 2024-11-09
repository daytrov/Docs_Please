import pygame
import sys
import os

WIDTH = 1820
HEIGHT = 980
FPS = 60

#os.chdir(os.path.dirname(os.path.dirname(__file__)))

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DOCS PLEASE')
clock = pygame.time.Clock()


background_image = pygame.image.load('images\\Background-img.jpg').convert_alpha()
background_image = pygame.transform.scale(background_image, (1820, 980))
passport_image = pygame.image.load('images\\паспорт.png').convert_alpha()
diploma_image = pygame.image.load('images\\Аттестат.png').convert_alpha()
snils_image = pygame.image.load('images\\снилс.png').convert_alpha()
application_image = pygame.image.load('images\\Заявление.png').convert_alpha()
minidocs = {
    "passport": {"rect": pygame.Rect(300, 500, 100, 150), "image": pygame.image.load("images\\паспорт_мини.png")},
    "diploma": {"rect": pygame.Rect(350, 550, 100, 150), "image": pygame.image.load("images\\аттестат_мини.png")},
    "snils": {"rect": pygame.Rect(400, 600, 100, 100), "image": pygame.image.load("images\\снилс_мини.png")},
    "application": {"rect": pygame.Rect(450, 650, 100, 150), "image": pygame.image.load("images\\заявление_мини.png")},
}
font = pygame.font.Font(None, 20)




class Character(pygame.sprite.Sprite):
    def __init__(self, x, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 500))
        self.is_hovered = False

    def update(self):
        if self.rect.x < WIDTH / 2 - 180:
            self.rect.x += 3
        else:
            self.rect.x = WIDTH / 2 - 180


class imageButton:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
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
computer = imageButton(1000, 500, 350, 350, '', 'images\\комп.png', 'images\\комп-hover.png', '')
table = imageButton(300, 500, 1400, 1000, '', 'images\\Table-PNG-Photos.png', '', '')
documents = imageButton(500, 500, 300, 300, '', 'images\\доки спрайт.png', '', '')
all_sprites.add(person)
form = imageButton(500, 200, 650, 650, "", 'images\\Заявление.png', '', '')

def draw_big_docs(key):
    match key:
        'passport':

        'diploma':

        'snils':

        'application':


def game_screen():
    selected_doc = None
    offset_x = 0
    offset_y = 0
    running = True
    index = -1
    while running:
        screen.blit(background_image, (0, 0))
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
                if event.button == 3:  # Левая кнопка мыши
                    for name, data in minidocs.items():
                        rect = data["rect"]
                        if rect.collidepoint(event.pos):
                            selected_doc = name
                            offset_x = rect.x - event.pos[0]
                            offset_y = rect.y - event.pos[1]
                            break

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:  # Отпускание левой кнопки
                    selected_doc = None

            elif event.type == pygame.MOUSEMOTION:
                if selected_doc:
                    # Перемещение выбранного документа
                    new_x = event.pos[0] + offset_x
                    new_y = event.pos[1] + offset_y

                    # Ограничение внутри большого прямоугольника
                    rect = minidocs[selected_doc]["rect"]
                    rect.x = max(table.rect.x, min(table.rect.x + table.rect.width - rect.width, new_x))
                    rect.y = max(table.rect.y, min(table.rect.y + table.rect.height - rect.height, new_y))

        for name, data in minidocs.items():
            rect = data["rect"]
            image = data["image"]
            # Приподнимаем выбранный документ
            if name == selected_doc:
                # Увеличиваем размеры изображения временно
                lifted_image = pygame.transform.scale(image, (rect.width + 10, rect.height + 10))
                lifted_rect = lifted_image.get_rect(center=rect.center)
                screen.blit(lifted_image, lifted_rect.topleft)
            else:
                # Обычное изображение
                scaled_image = pygame.transform.scale(image, rect.size)
                screen.blit(scaled_image, rect.topleft)


        if index % 2 == 0:
            asdf = 1
            #отрубил пока
            #form.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    game_screen()