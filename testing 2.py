import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (173, 216, 230)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
BUTTON_COLOR = (100, 100, 255)

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Несколько прямоугольников")
clock = pygame.time.Clock()

# Шрифт
font = pygame.font.Font(None, 24)

# Данные для прямоугольников и кнопок
rectangles = [
    {"rect": pygame.Rect(200, 50, 400, 500), "close_button": None, "is_visible": False, "text": "Прямоугольник 1"},
    {"rect": pygame.Rect(200, 50, 400, 500), "close_button": None, "is_visible": False, "text": "Прямоугольник 2"},
    {"rect": pygame.Rect(200, 50, 400, 500), "close_button": None, "is_visible": False, "text": "Прямоугольник 3"},
    {"rect": pygame.Rect(200, 50, 400, 500), "close_button": None, "is_visible": False, "text": "Прямоугольник 4"},
]

# Создаём кнопки для отображения прямоугольников
buttons = [
    {"button_rect": pygame.Rect(50, 520, 150, 40), "color": BUTTON_COLOR, "text": "Показать 1"},
    {"button_rect": pygame.Rect(250, 520, 150, 40), "color": BUTTON_COLOR, "text": "Показать 2"},
    {"button_rect": pygame.Rect(450, 520, 150, 40), "color": BUTTON_COLOR, "text": "Показать 3"},
    {"button_rect": pygame.Rect(650, 520, 150, 40), "color": BUTTON_COLOR, "text": "Показать 4"},
]

# Инициализация кнопок закрытия
for rectangle in rectangles:
    rect = rectangle["rect"]
    rectangle["close_button"] = pygame.Rect(rect.right - 30, rect.top + 10, 20, 20)

# Переменные для перемещения
is_dragging = False
selected_rect = None
offset_x, offset_y = 0, 0

# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        # Начало перетаскивания (правая кнопка мыши)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for i, rect_data in enumerate(rectangles):
                if rect_data["is_visible"] and rect_data["rect"].collidepoint(event.pos):
                    is_dragging = True
                    selected_rect = rect_data
                    offset_x = rect_data["rect"].x - event.pos[0]
                    offset_y = rect_data["rect"].y - event.pos[1]

                    # Перемещаем текущий прямоугольник в конец списка
                    rectangles.append(rectangles.pop(i))
                    break

        # Нажатие левой кнопкой мыши
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Проверка нажатия на кнопки показа
            for i, button_data in enumerate(buttons):
                if button_data["button_rect"].collidepoint(event.pos):
                    rectangles[i]["is_visible"] = True

            # Проверка нажатия на кнопки закрытия
            for rect_data in rectangles:
                if rect_data["is_visible"] and rect_data["close_button"].collidepoint(event.pos):
                    rect_data["is_visible"] = False

        # Остановка перетаскивания
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            is_dragging = False
            selected_rect = None

        # Перемещение прямоугольника
        elif event.type == pygame.MOUSEMOTION and is_dragging and selected_rect:
            selected_rect["rect"].x = event.pos[0] + offset_x
            selected_rect["rect"].y = event.pos[1] + offset_y
            selected_rect["close_button"].x = selected_rect["rect"].right - 30
            selected_rect["close_button"].y = selected_rect["rect"].top + 10

    # Рисование
    screen.fill(WHITE)

    # Рисуем кнопки показа
    for button_data in buttons:
        pygame.draw.rect(screen, button_data["color"], button_data["button_rect"])
        button_text = font.render(button_data["text"], True, WHITE)
        button_text_rect = button_text.get_rect(center=button_data["button_rect"].center)
        screen.blit(button_text, button_text_rect)

    # Рисуем прямоугольники, если они видимы
    for rect_data in rectangles:
        if rect_data["is_visible"]:
            pygame.draw.rect(screen, BLUE, rect_data["rect"])  # Прямоугольник
            pygame.draw.rect(screen, BLACK, rect_data["rect"], 2)  # Обводка

            # Рисуем кнопку закрытия
            pygame.draw.rect(screen, RED, rect_data["close_button"])

            # Рисуем текст внутри прямоугольника
            x, y = rect_data["rect"].x + 20, rect_data["rect"].y + 20  # Отступы внутри прямоугольника
            text_surface = font.render(rect_data["text"], True, BLACK)
            screen.blit(text_surface, (x, y))

    pygame.display.flip()
    clock.tick(60)
