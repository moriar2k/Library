from django.db import models
import random


# Create your models here.

class Bookshelf(models.Model):
    kind = models.TextField(default='')
    title = models.TextField(default='')
    author = models.TextField(default='')
    epoch = models.TextField(default='')
    genre = models.TextField(default='')
    quantity = models.IntegerField(default=random.randint(0, 10))
