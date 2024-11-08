import pygame
from sys import exit

WIDTH, HEIGHT = (1024, 768)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Joe mama")
clock = pygame.time.Clock()


class imageButton:
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft = (x, y))

    def draw(self):
        WIN.blit(self.image, self.rect.topleft)


button_img = pygame.image.load("..\\images\\комп-hover.png")
form = pygame.image.load("..\\images\person.png")


index = -1




button = imageButton(100, 100, 350, 350,"..\\images\\комп-hover.png")
form = imageButton(100,100, 100, 100, "..\\images\person.png")

while True:
    WIN.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if button.rect.collidepoint(event.pos):
                    index += 1

    button.draw()
    if index % 2 == 0:
        form.draw()


    pygame.display.update()
    clock.tick(60)