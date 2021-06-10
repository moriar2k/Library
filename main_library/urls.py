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
    path('index/details/<int:id>', views.details, name = 'details'),
    path("register/", views.register_request, name="register"),
    path('index/details/<int:id>/rent', views.rent, name = 'rent'),
<<<<<<< HEAD
=======
    path('user_view/', views.user_view, name='user_view'),
    path('index/details/<int:id>/return', views.return_book, name = 'return_book')
>>>>>>> 629dcdea52361b94bcb1f3203b893bd099d51585
    ]