import requests
from main_library.models import Bookshelf
import random

# uruchamianie z manage.py shell za pomocą komendy exec(open('Wgrywka danych.py').read())

r = requests.get('https://wolnelektury.pl/api/books/').json()
for x in r:
    rand_quantity = random.randint(0, 10)
    Bookshelf.objects.create(kind=x['kind'], title=x['title'], author=x['author'],
                             epoch=x['epoch'], genre=x['genre'], quantity=rand_quantity)