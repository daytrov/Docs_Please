import pygame
import sys
import os
import BD_api

WIDTH = 1820
HEIGHT = 980
FPS = 60
BD_api.first_iteration()
abitur_info = BD_api.get_info(False)
lier_abitur_info = BD_api.liar()

#os.chdir(os.path.dirname(os.path.dirname(__file__)))

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('music\\Neon Dreams.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.01)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DOCS PLEASE')
clock = pygame.time.Clock()

sound = pygame.mixer.Sound('music\\Neon Dreams.mp3')

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
big_docs = {
    "passport": {"rect": pygame.Rect(200, 50, 400, 500), "close_button": None, "is_visible": False, "image": pygame.image.load("images\\паспорт.png")},
    "diploma": {"rect": pygame.Rect(200, 50, 400, 500), "close_button": None, "is_visible": False, "image": pygame.image.load("images\\Аттестат.png")},
    "snils": {"rect": pygame.Rect(200, 50, 400, 500), "close_button": None, "is_visible": False, "image": pygame.image.load("images\\снилс.png")},
    "application": {"rect": pygame.Rect(200, 50, 400, 500), "close_button": None, "is_visible": False, "image": pygame.image.load("images\\Заявление.png")},
}
for name, rectangle in big_docs.items():
    rect = rectangle["rect"]
    rectangle["close_button"] = pygame.Rect(rect.right - 30, rect.top + 10, 20, 20)

font = pygame.font.Font(None, 24)
italic_font = pygame.font.Font(None, 24)
italic_font.set_italic(True)




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
form = imageButton(500, 200, 650, 650, "", 'images\\form_comp.jpg', '', '')
start_button = imageButton(WIDTH/2-(252/2), 600, 252, 78, "", "images\\Start-game.png", "images\\Start-game-hover.png", "sound\\startbut-sound.mp3")
settings_button = imageButton(WIDTH/2-(252/2), 700, 252, 78, "", "images\\Settings-button.png", "images\\Settings-button-hover.png", "sound\\startbut-sound.mp3")
logo_image = pygame.image.load('images\\logo.png').convert_alpha()
background_image = pygame.image.load('images\\Background-img.jpg').convert_alpha()
background_image = pygame.transform.scale(background_image, (1820, 980))
back_button = imageButton(WIDTH/2-(252/2), 600, 252, 78, "", "images\\Back-button.png", "images\\Back-button-hover.png", "sound\\startbut-sound.mp3")


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

def game_screen():
    global big_docs
    selected_doc = None
    offset_x = 0
    offset_y = 0
    running = True
    index = -1
    is_dragging = False
    selected_big_doc = None
    running = True
    while running:
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)
        clock.tick(FPS)
        table.draw(screen)
        person.update()
        for interaction_items in [table, computer, documents]:
            interaction_items.draw(screen)
            interaction_items.check_hover(pygame.mouse.get_pos())

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if computer.rect.collidepoint(event.pos):
                        index += 1
            # Нажатие мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Правая кнопка мыши: перемещение mini_docs
                if event.button == 3:
                    for name, data in minidocs.items():
                        rect = data["rect"]
                        if rect.collidepoint(event.pos):
                            selected_doc = name
                            offset_x = rect.x - event.pos[0]
                            offset_y = rect.y - event.pos[1]
                            break

                    for name, rect_data in big_docs.items():
                        if rect_data["is_visible"] and rect_data["rect"].collidepoint(event.pos):
                            is_dragging = True
                            selected_big_doc = rect_data
                            offset_x = rect_data["rect"].x - event.pos[0]
                            offset_y = rect_data["rect"].y - event.pos[1]

                            # Перемещение big_docs на передний план
                            big_docs = {k: v for k, v in big_docs.items() if k != name}  # Удаляем выбранный элемент
                            big_docs[name] = selected_big_doc  # Добавляем его в конец
                            break


                # Левая кнопка мыши: открытие big_docs
                elif event.button == 1:
                    for i, (name, data) in enumerate(minidocs.items()):
                        if data["rect"].collidepoint(event.pos):
                            # Показываем соответствующий big_docs
                            big_doc = big_docs[name]
                            big_doc["rect"] = pygame.Rect(
                                data["rect"].x, data["rect"].y,
                                big_doc["image"].get_width(), big_doc["image"].get_height()
                            )
                            # Расчёт позиции кнопки закрытия
                            big_doc["close_button"] = pygame.Rect(
                                big_doc["rect"].right - 30,
                                big_doc["rect"].top + 10,
                                20, 20
                            )
                            big_doc["is_visible"] = True
                            break

                    # Проверка кнопки закрытия
                    for rect_data in big_docs.values():
                        if rect_data["is_visible"] and rect_data["close_button"].collidepoint(event.pos):
                            rect_data["is_visible"] = False

            # Отпускание правой кнопки мыши
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                selected_doc = None
                is_dragging = False
                selected_big_doc = None

            # Перемещение объектов
            elif event.type == pygame.MOUSEMOTION:
                # Перемещение mini_docs
                if selected_doc:
                    rect = minidocs[selected_doc]["rect"]
                    rect.x = event.pos[0] + offset_x
                    rect.y = event.pos[1] + offset_y

                # Перемещение big_docs
                elif is_dragging and selected_big_doc:
                    selected_big_doc["rect"].x = event.pos[0] + offset_x
                    selected_big_doc["rect"].y = event.pos[1] + offset_y
                    # Перемещаем кнопку закрытия
                    selected_big_doc["close_button"].x = selected_big_doc["rect"].right - 30
                    selected_big_doc["close_button"].y = selected_big_doc["rect"].top + 10

        # Рисование mini_docs
        for name, data in minidocs.items():
            rect = data["rect"]
            image = data["image"]
            screen.blit(pygame.transform.scale(image, rect.size), rect.topleft)

        # Рисование big_docs
        for name, rect_data in big_docs.items():
            if rect_data["is_visible"]:
                screen.blit(rect_data["image"], rect_data["rect"].topleft)
                pygame.draw.rect(screen, (255, 0, 0), rect_data["close_button"])
                match name:
                    case "passport":
                        text_surface = font.render(f"{abitur_info['PasportOtd']}", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 90, rect_data["rect"].y + 60))
                        text_surface = font.render(f"{abitur_info['PasportDate']}", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 140, rect_data["rect"].y + 100))
                        text_surface = font.render(f"{abitur_info['PasportNum'][0:5]}", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 400, rect_data["rect"].y + 100))
                        text_surface = font.render(f"{abitur_info['PasportCode']}", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 215, rect_data["rect"].y + 130))
                        text_surface = font.render(f"{abitur_info['PasportNum'][4:]}", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 400, rect_data["rect"].y + 130))
                        text_surface = italic_font.render(f"{abitur_info['LastName']} {abitur_info['FirstName'][0]}. {abitur_info['FatherName'][0]}.", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 360, rect_data["rect"].y + 315))
                        text_surface = font.render(f"{abitur_info['LastName']}", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 290, rect_data["rect"].y + 400))
                        text_surface = font.render(f"{abitur_info['FirstName']}", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 290, rect_data["rect"].y + 435))
                        text_surface = font.render(f"{abitur_info['FatherName']}", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 290, rect_data["rect"].y + 470))
                        text_surface = font.render(f"{abitur_info['Gender'][0]}", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 245, rect_data["rect"].y + 500))
                        text_surface = font.render(f"{abitur_info['DateOfBirth']}", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 430, rect_data["rect"].y + 500))
                        text_surface = font.render(f"{abitur_info['Address']}", True, (0, 0, 0))
                        screen.blit(text_surface, (rect_data["rect"].x + 185, rect_data["rect"].y + 560))
                        screen.blit(text_surface, (rect_data["rect"].x + 185, rect_data["rect"].y + 640))
                    #case "diploma":

                    #case "snils":

                    #case "application":
        if index % 2 == 0:
            form.draw(screen)
            Abir_data = font.render("ДАННЫЕ АБИТУРИЕНТА", True, (0,0,0))
            screen.blit(Abir_data, (550, 230))
            PasportNum = font.render(f"Серия и номер паспорта: {abitur_info['PasportNum']}", True, (0,0,0))
            screen.blit(PasportNum, (550, 250))
            PasportCode = font.render(f"Номер подразделения: {abitur_info['PasportCode']}", True, (0,0,0))
            screen.blit(PasportCode, (550, 270))
            PasportOtd = font.render(f"Кем выдан: {abitur_info['PasportOtd']}", True, (0,0,0))
            screen.blit(PasportOtd, (550, 290))
            PasportDate = font.render(f"Дата выдачи: {abitur_info['PasportDate']}", True, (0,0,0))
            screen.blit(PasportDate, (550, 310))
            DateOfBirth = font.render(f"Дата рождения: {abitur_info['DateOfBirth']}", True, (0,0,0))
            screen.blit(DateOfBirth, (550, 330))
            FirstName = font.render(f"Имя: {abitur_info['FirstName']}", True, (0,0,0))
            screen.blit(FirstName, (550, 350))
            LastName = font.render(f"Фамилия: {abitur_info['LastName']}", True, (0,0,0))
            screen.blit(LastName, (550, 370))
            FatherName = font.render(f"Отчество: {abitur_info['Address']}", True, (0,0,0))
            screen.blit(FatherName, (550, 390))
            Living_place = font.render(f"Адресс регистрации: {abitur_info['Address']}", True, (0,0,0))
            screen.blit(Living_place, (550, 410))
            screen.blit(Living_place, (550, 430))

        pygame.display.flip()



if __name__ == "__main__":
    start_menu()