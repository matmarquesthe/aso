from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.


def home(request):
    now = datetime.datetime.now()
    # html = "<html><body> Data e hora do sistema: %s, </body><html>"% now

    return render(request, 'funcionario/home.html')


