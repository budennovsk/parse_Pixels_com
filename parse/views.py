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

    # print(os.getcwd())
    # with open('media/hackr/38275.jpeg', 'rb') as f:
    #     print(f.name)
    #     ph = 'http://127.0.0.1:8000/' + f.name
    #     df = Data.objects.create(img='/hackr/38275.jpeg')
    #     df
    # # df = Data()
    # df.img_file.save('1.png', File(open('media/specs/1.png', 'rb')))

    form = FileForm()
    return render(request, 'parse/index.html', {'data': data, 'form': form})
