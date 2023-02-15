import os

import pygame
import requests


coords = [37.6156, 55.7522]
size = 10
map_request = f'https://static-maps.yandex.ru/1.x/?ll={coords[0]},{coords[1]}&z={size}&l=map'
response = requests.get(map_request)

map_file = 'map.png'
with open(map_file, 'wb') as file:
    file.write(response.content)

pygame.init()
pygame.display.set_caption('Большая задача по Maps API. Часть №1 | Чалдаев')
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

os.remove(map_file)
