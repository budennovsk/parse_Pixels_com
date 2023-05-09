import os

from django.shortcuts import render, redirect

from .models import Data
from .forms import *
from .scraping import *
from .API_scraping import get_scrap


# Create your views here.
def index(request: object) -> render:
    """ Получает запросы в виде поиска со страницы, в виде формы запросов"""
    # get_request(url) добавляет картинки в бд через скрипт без API

    # добавляет через форму информацию в БД
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    # добавляет в БД картинки из поиска, запускает парсинг сервиса по API
    search_data = request.GET.get('query', '')
    get_scrap(query=search_data)
    data = Data.objects.all()
    os.chdir(r'E:\Django\parse_Pixels_com\media')
    # создание каталог результатов поиска локально
    for root, dirs, files in os.walk(search_data):

        for _file in files:

            with open(f'{root}\{_file}', 'rb') as f:
                # ph = 'http://127.0.0.1:8000/' + f.name
                if not Data.objects.filter(img=f.name).exists():
                    Data.objects.create(img=f.name)

    form = FileForm()
    return render(request, 'parse/index.html', {'data': data, 'form': form})
