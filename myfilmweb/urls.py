from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rejestracja/', user_views.register, name='register'),
    path('logowanie/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', include('filmweb.urls')),
]
