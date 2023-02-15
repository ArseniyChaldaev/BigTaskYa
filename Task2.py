import pygame
import requests

coords = [37.6156, 55.7522]
size = 10


def load_the_map(z):
    map_request = f'https://static-maps.yandex.ru/1.x/?ll={coords[0]},{coords[1]}&z={z}&l=map'
    response = requests.get(map_request)
    map_file = f'assets/map.png'
    with open(map_file, 'wb') as file:
        file.write(response.content)
    return pygame.image.load(map_file)


map_images = [load_the_map(i) for i in range(3, 18)]

FPS = 5
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Большая задача по Maps API. Часть №2 | Чалдаев')
screen = pygame.display.set_mode((600, 450))
running = True
changed = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEDOWN and size > 3:
                size -= 1
                changed = True
            elif event.key == pygame.K_PAGEUP and size < 17:
                size += 1
                changed = True
    if changed:
        screen.blit(load_the_map(size), (0, 0))
        pygame.display.flip()
        changed = False
    clock.tick(FPS)
pygame.quit()
