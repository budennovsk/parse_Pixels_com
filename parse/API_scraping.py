import math
import os.path
import pprint

from password import API_KEY
import requests
import json
from tqdm import tqdm


KEY = API_KEY

def get_scrap(query='') -> str:
    """Получает запрос с HTML страницы на поиск"""

    # авторизация, передача токена на API запрос
    headers = {"Authorization": KEY}
    query_str = f'https://api.pexels.com/v1/search?query={query}&per_page=80&orientation=landscape'
    response = requests.get(url=query_str, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        return f'Ошибка: {response.status_code}'

    # создание название
    img_dir_path = '_'.join(i for i in query.split(' ') if i.isalnum())
    os.chdir(os.pardir)
    c = os.getcwd()

    # создание json файла
    if not os.path.exists(f'{c}/media/{img_dir_path}'):
        os.makedirs(f'{c}/media/{img_dir_path}')
    json_data = response.json()
    # pprint.pprint(json_data,indent=4)

    # создание папки
    with open(f'parse/json/result_{query}.json', 'w', encoding="utf-8") as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)

    image_count = json_data.get('total_results')

    # скачивание URL
    if not json_data.get('next_page'):
        img_urls = [i.get('src').get('original') for i in json_data.get('photos')]
        download_img(img_lst=img_urls, img_dir_path=img_dir_path)

    else:
        print('ddd')
        # проход по всем страницам в поиске
        print(f'Всего изображений {image_count}')
        img_lst_urls = []
        for page in range(1, math.ceil(image_count / 80) + 1):
            query_str = f'{query_str}&page={page}'
            response = requests.get(url=query_str, headers=headers)
            json_data = response.json()
            img_urls = [i.get('src').get('original') for i in json_data.get('photos')]
            img_lst_urls.extend(img_urls)

        # передача URL на скачивание
        download_img(img_lst=img_lst_urls, img_dir_path=img_dir_path)


def download_img(img_lst=[], img_dir_path='') -> None:
    """ Скачивание image из URL"""
    for i in tqdm(img_lst):

        response = requests.get(url=i)
        if response.status_code == 200:
            with open(f'./media/{img_dir_path}/{i.split("-")[-1]}', 'wb') as file:
                file.write(response.content)


if __name__ == '__main__':
    get_scrap(query='')
