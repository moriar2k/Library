from django.db import models
from django.contrib.auth.models import User
import random


# Create your models here.

class Bookshelf(models.Model):
    kind = models.TextField(default='')
    title = models.TextField(default='')
    author = models.TextField(default='')
    epoch = models.TextField(default='')
    genre = models.TextField(default='')
    quantity = models.IntegerField(default=random.randint(0, 10))

class RentalList(models.Model):
<<<<<<< HEAD
    book_id = models.ForeignKey(Bookshelf, default=None, on_delete=models.SET_DEFAULT)
    user_id = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT)
    check_out_date = models.DateTimeField(auto_now_add=True)
    planned_date_of_return = models.DateTimeField(default=None)
    date_of_return = models.DateTimeField(default=None)
=======
    book_id = models.ForeignKey(Bookshelf, default=None, on_delete=models.SET_DEFAULT, null=True)
    user_id = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT)
    check_out_date = models.DateTimeField(auto_now_add=True)
    planned_date_of_return = models.DateTimeField(default=None, null=True)
    date_of_return = models.DateTimeField(default=None, null=True)
>>>>>>> 629dcdea52361b94bcb1f3203b893bd099d51585
    status = models.TextField(default='Active')
