import pygame
import requests
from io import BytesIO
from PIL import Image


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

