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

class Rental_list(models.Model):
    book_id = models.IntegerField(default=None)
    user_id = models.IntegerField(default=None)
    check_out_date = models.DateTimeField(auto_now_add=True)
    planned_date_of_return = models.DateTimeField(default=None)
    date_of_return = models.DateTimeField(default=None)
    status = models.TextField(default='Active')
