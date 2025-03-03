# max

import argparse
import os
import sys
import pygame
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--coord1", metavar="crd1", type=str)
parser.add_argument("--coord2", metavar="crd2", type=str)
parser.add_argument("--scale1", metavar='scl1', type=str)
parser.add_argument("--scale2", metavar='scl2', type=str)
args = parser.parse_args()
try:
    crt = [args.coord1, args.coord2]
    csl = [args.scale1, args.scale2]


    def show_map(ll_spn=None, map_type='map'):
        if ll_spn:
            map_request = f'https://static-maps.yandex.ru/1.x/?{ll_spn}&l={map_type}'
        else:
            map_request = f'https://static-maps.yandex.ru/1.x/?&l={map_type}'


    server_address = 'https://static-maps.yandex.ru/v1?'
    api_key = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
    ll_spn = f'll={crt[0]},{crt[1]}&spn={csl[0]},{csl[1]}'
    # Готовим запрос.

    map_request = f"{server_address}{ll_spn}&apikey={api_key}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    pygame.init()

    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
    os.remove(map_file)
except Exception:
    print("некоректный ввод")
