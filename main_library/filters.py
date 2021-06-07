# from django.contrib.auth.models import User
import django_filters
from django_filters import CharFilter, ModelMultipleChoiceFilter
from .models import Bookshelf
from django import forms


class UserFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(lookup_expr='icontains', label="Tytul")
    author = django_filters.CharFilter(lookup_expr='icontains', label="Autor")
    genre = django_filters.CharFilter(lookup_expr = 'icontains', label="Rodzaj")
    # genre = django_filters.ModelMultipleChoiceFilter(queryset=Bookshelf.objects.value('genre'),
    #                                                  widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Bookshelf
        fields = ['title', 'author', 'genre']
