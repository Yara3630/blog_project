from django.shortcuts import render
from http import HTTPStatus


def error403(request, reason=''):
    return render(request, 'core/403.html')


def error404(request, exception):
    context = {'path': request.path, }
    return render(request,
                  'core/404.html',
                  context,
                  status=HTTPStatus.NOT_FOUND)
