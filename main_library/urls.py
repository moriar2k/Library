from django.urls import path, include
from . import views
from .filters import UserFilter
from django_filters.views import FilterView

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('index/', views.index, name = 'index'),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    # path('<int:question_id>', views.detail, name='detail'),
    path('index/wypozycz/<int:id>', views.wypozycz, name = 'wypozycz'),
    path("register", views.register_request, name="register"),
    ]