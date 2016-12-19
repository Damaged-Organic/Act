# act_project/act/website/views.py
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def handler404(request):
    return JsonResponse({'detail': "Не знайдено."}, status=404)


def handler500(request):
    return JsonResponse({'detail': "Internal Server Error."}, status=500)
