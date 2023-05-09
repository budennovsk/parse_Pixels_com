from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from parse.models import *

URL = 'https://pixels.com/art/abstract'


def get_request(url: str) -> None:
    """ Парсит сайт без API через bs4, вызов происходит через views"""

    # установка произвольная значения
    number_page = 1
    img_number = 0
    for _ in tqdm(range(2)):
        gt = requests.get(url)

        # варим суп
        soup = BeautifulSoup(gt.text, "html.parser")
        all_n = soup.find_all(class_="flowImageContainerDiv")
        for i in tqdm(all_n):
            rec_a = i.find('a')
            link = str(*[n.get('data-src') for n in rec_a])

            # добавляем в БД image
            Data.objects.create(img_url=link)

            with open(f'parse/parse_img/{img_number}.png', 'wb') as file:
                file.write(requests.get(link).content)
            img_number += 1
        number_page += 1


print("Файл скачен")

if __name__ == '__main__':
    get_request(URL)
