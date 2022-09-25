from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from pkg_resources import require


class Word(models.Model):
    name = models.CharField(max_length=50)
    author_translation = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Translation(models.Model):
    name = models.CharField(max_length=50)
    part_of_speech = models.CharField(max_length=50)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

class Definition(models.Model):
    name = models.CharField(max_length=50)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)