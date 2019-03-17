from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Movie


def home(request):
    return render(request, 'filmweb/home/home.html', {'movies': Movie.objects.all()})

class MovieListView(ListView):
    model = Movie
    template_name = 'filmweb/home/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'movies'
    # ordering = najwyższa ocena
    paginate_by = 10


class MovieDetailView(DetailView):
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'description', 'image_thumbnail', 'release_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
