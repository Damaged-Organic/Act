# act_project/act/website/views_error.py
from django.http import JsonResponse
from django.shortcuts import render


def handler400(request):
    status = 400

    if request.is_ajax():
        response = JsonResponse(
            {'detail': "Неправильний запит."}, status=status)
    else:
        response = render(
            request, 'website/errors/400.html', {}, status=status)

    return response


def handler403(request):
    status = 403

    if request.is_ajax():
        response = JsonResponse(
            {'detail': "Заборонено."}, status=status)
    else:
        response = render(
            request, 'website/errors/403.html', {}, status=status)

    return response


def handler404(request):
    status = 404

    if request.is_ajax():
        response = JsonResponse(
            {'detail': "Не знайдено."}, status=status)
    else:
        response = render(
            request, 'website/errors/404.html', {}, status=status)

    return response


def handler500(request):
    status = 500

    if request.is_ajax():
        response = JsonResponse(
            {'detail': "Внутрішня помилка серверу."}, status=status)
    else:
        response = render(
            request, 'website/errors/500.html', {}, status=status)

    return response
