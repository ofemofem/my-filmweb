from django.urls import path
from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView
)

urlpatterns = [
    path('', MovieListView.as_view(), name='home-filmweb'),
    path('film/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('film/nowy/', MovieCreateView.as_view(), name='movie-create'),
]
