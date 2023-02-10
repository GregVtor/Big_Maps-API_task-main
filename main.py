import pygame
import requests
from io import BytesIO


pygame.init()
pygame.display.set_caption('Maps')
window_size = (450, 450)

screen = pygame.display.set_mode(window_size)


def pars(x, y, zoom):
    params = {
        'll': f'{x},{y}',
        'size': '450,450',
        'l': 'sat,skl',
        'z': zoom,
    }
    rec = requests.get(f'https://static-maps.yandex.ru/1.x/', params=params)
    img = BytesIO(rec.content)

    return img


image = pygame.image.load(pars(37.677751, 55.757718, 13)).convert_alpha()

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(image, (0, 0))
    pygame.display.flip()
pygame.quit()