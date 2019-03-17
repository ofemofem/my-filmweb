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

class UserMovieListView(ListView):
    model = Movie
    template_name = 'filmweb/user_movies.html'
    context_object_name = 'movies'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Movie.objects.filter(author=user) #.order_by najwyższa ocena

class MovieDetailView(DetailView):
    model = Movie


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'description', 'image_thumbnail', 'release_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
