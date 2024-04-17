from django.shortcuts import render
from .models import Mesures


def index(request):

    data = Mesures.objects.all().values().first()

    return render(request, 'appAquaponie/index.html', {
        'data': data
    })
