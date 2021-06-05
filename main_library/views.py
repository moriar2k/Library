from django.shortcuts import render
from django.http import HttpResponse
from .models import Bookshelf
from django.contrib.auth.models import User
from .filters import UserFilter


# Create your views here.
def home_page(request):
    return render(request, 'main_library/home_page.html', {})


def index(request):
    obj = Bookshelf.objects.values('title', 'author', 'genre','kind', 'epoch')
    table_filter = UserFilter(request.GET, queryset=obj)
    # obj = myFilter.qs
    return render(
        request,
        'main_library/index.html',
        {'all_books': obj, 'table_filter': table_filter}
    )


