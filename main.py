import pygame
import requests
from io import BytesIO
from PIL import Image


pygame.init()
pygame.display.set_caption('Maps')
window_size = (800, 800)

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

map_image = pygame.image.load(pars(int(input())), int(input()), 13)
image = pygame.transform.scale(map_image, (400, 400))


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()