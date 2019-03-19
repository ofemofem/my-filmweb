from django.urls import path
from . import views
from .views import (
    MovieDetailView,
    MovieCreateView
)

urlpatterns = [
    path('', views.home, name='home-filmweb'),
    path('film/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('film/nowy/', MovieCreateView.as_view(), name='movie-create'),
]
