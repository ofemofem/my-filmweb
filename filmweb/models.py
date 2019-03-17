from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image_thumbnail = models.TextField()
    release_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

