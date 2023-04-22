import os

from django.core.files import File
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Data
from .forms import *
from .scraping import *


# Create your views here.
def index(request):
    # get_request(url) добавляет картинки в бд
    if request.method == "POST":

        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    data = Data.objects.all()
    os.chdir(r'E:\Django\parse_Pixels_com\media')
    for root, dirs, files in os.walk('hackr'):

        for _file in files:

            with open(f'{root}\{_file}', 'rb') as f:
                # ph = 'http://127.0.0.1:8000/' + f.name
                if not Data.objects.filter(img=f.name).exists():
                    Data.objects.create(img=f.name)

    form = FileForm()
    return render(request, 'parse/index.html', {'data': data, 'form': form})
