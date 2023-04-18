from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from parse.models import Data
from .forms import *
from .scraping import *

# Create your views here.
def index(request):

    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    data = Data.objects.all()


    form = FileForm()
    return render(request, 'parse/index.html', {'data': data, 'form': form})
