# act_project/act/website/views.py
from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')
