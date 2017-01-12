# act_project/act/website/views.py
from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')


def handler400(request):
    return JsonResponse({'detail': "Неправильний запит."}, status=400)


def handler403(request):
    return JsonResponse({'detail': "Заборонено."}, status=403)


def handler404(request):
    return JsonResponse({'detail': "Не знайдено."}, status=404)


def handler500(request):
    return JsonResponse({'detail': "Внутрішня помилка серверу."}, status=500)
