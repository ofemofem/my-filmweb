from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Movie, New


def home(request):
    movies = Movie.objects.filter().order_by('pub_date')[0:3]
    news = New.objects.filter().order_by('pub_date')[0:3]
    return render(request, 'filmweb/home/home.html', {'movies': movies, 'news': news})


class MovieDetailView(DetailView):
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'description', 'image_thumbnail', 'release_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
