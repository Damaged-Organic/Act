# act_project/act/website/views_error.py
from django.http import JsonResponse


def handler400(request):
    return JsonResponse({
        'detail': "Неправильний запит."
    }, status=400)


def handler403(request):
    return JsonResponse({
        'detail': "Заборонено."
    }, status=403)


def handler404(request):
    return JsonResponse({
        'detail': "Не знайдено."
    }, status=404)


def handler500(request):
    return JsonResponse({
        'detail': "Внутрішня помилка серверу."
    }, status=500)
