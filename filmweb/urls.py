from django.urls import path
from .views import (
    MovieListView,
    UserMovieListView,
    MovieDetailView,
    MovieCreateView
)

urlpatterns = [
    path('', MovieListView.as_view(), name='home-filmweb'),
    path('user/<str:username>', UserMovieListView.as_view(), name='user-movies'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movie/new/', MovieCreateView.as_view(), name='movie-create'),
]
