import pygame
import requests

coords = [37.6156, 55.7522]
size = 10
lon, lat = coords


def load_the_map(z, lon, lat):
    map_request = f'https://static-maps.yandex.ru/1.x/?ll={lon:9.6f},{lat:9.6f}&z={z}&l=map'
    map_file = f'assets/map.png'
    response = requests.get(map_request)
    if response.status_code == 200:
        with open(map_file, 'wb') as file:
            file.write(response.content)
    return pygame.image.load(map_file)


FPS = 25
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Большая задача по Maps API. Часть №3 | Чалдаев')
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
            elif event.key == pygame.K_UP and lat < 90:
                lat += 0.1
                changed = True
            elif event.key == pygame.K_DOWN and lat > -90:
                lat -= 0.1
                changed = True
            elif event.key == pygame.K_LEFT and lon > -180:
                lon -= 0.1
                changed = True
            elif event.key == pygame.K_RIGHT and lon < 180:
                lon += 0.1
                changed = True
    if changed:
        screen.blit(load_the_map(size, lon, lat), (0, 0))
        pygame.display.flip()
        changed = False
    clock.tick(FPS)
pygame.quit()
