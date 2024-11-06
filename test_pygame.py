import pygame
import BD_api
import podpis

width = 1820
height = 980
FPS = 60

BD_api.first_iteration()
personal_dict = [
    'LastName',
    'FirstName',
    'FatherName',
    'Gender',
    'DateOfBirth',
    'YearsOld',
    'Phone',
    'Login',
    'Password',
    'Email',
    'Address',
    'Country',
    'Region',
    'City',
    'Street',
    'Apartment',
    'House',
    'PasportNum',
    'PasportCode',
    'PasportOtd',
    'PasportDate',
    'inn_fiz',
    'snils',
    'oms',
    'bankBIK',
    'bankCorr',
    'bankINN',
    'bankNum',
    'bankClient',
    'bankCard',
    'bankDate',
    'bankCVC',
]
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Доки плиз")
clock = pygame.time.Clock()

test_image = pygame.image.load('D:/PyCharmProjects/Docs_Please/images/office.jpg')

clock.tick(FPS)
screen.fill((60, 255, 150))
surface = pygame.Surface((100,100))
screen.blit(pygame.transform.scale(test_image, (width, height)), (0, 0))
button_rect = pygame.Rect(200, 250, 130, 50)
pygame.draw.rect(screen, (0, 255, 0), button_rect)
font = pygame.font.Font(None, 36)
text = font.render("Инфа", True, (0, 0, 0))
screen.blit(text, (button_rect.x + 10, button_rect.y + 10))
button_passport = pygame.Rect(200, 200, 130, 50)
pygame.draw.rect(screen, (0, 255, 0), button_passport)
screen.blit(font.render("Паспорт", True, (0, 0, 0)), (button_passport.x + 10, button_passport.y + 10))
pygame.display.flip()



def draw_inf():
    abitur_info = BD_api.get_info(True)
    #podpis.get_img(abitur_info["FirstName"], abitur_info["LastName"], abitur_info["FatherName"])
    #screen.blit(pygame.transform.scale(pygame.image.load('D:/PyCharmProjects/Docs_Please/podpis.png'), (250, 250)), (900, 700))
    pygame.draw.rect(screen, (255, 255, 255), (800, 100, 800, 900))
    pygame.draw.rect(screen, (240,240,240), (50,50,1550, 100))
    for posAbitur in range(len(abitur_info)):
        text1 = font.render(str(abitur_info[personal_dict[posAbitur]]), True, (0, 0, 0))
        screen.blit(text1, (830, 100 + posAbitur*25))
    pygame.display.flip()

def draw_pasport():
    opp = True


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                draw_inf()
