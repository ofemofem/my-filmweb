from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_thumbnail = models.CharField(max_length=150)
    release_date = models.DateField()
    pub_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class New(models.Model):
    image_news = models.CharField(max_length=150)
    pub_date = models.DateTimeField(default=timezone.now)
