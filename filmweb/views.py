from django.shortcuts import render
from .models import Movie


def home(request):
    return render(request, 'filmweb/home/home.html', {'movies': Movie.objects.all()})