from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('index/', views.index, name = 'index'),
    ]