from django.urls import path, include
from . import views
from .filters import UserFilter
from django_filters.views import FilterView

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('index/', views.index, name = 'index'),
    ]