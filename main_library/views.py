from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from .models import Bookshelf, RentalList
from django.contrib.auth.models import User
from .filters import UserFilter
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def home_page(request):
    username = request.user
    return render(request, 'main_library/home_page.html', {'login': username})


def index(request):
    obj = Bookshelf.objects.values('title', 'author', 'genre', 'kind', 'epoch', 'quantity', 'id')
    table_filter = UserFilter(request.GET, queryset=obj)
    # obj = myFilter.qs
    return render(
        request,
        'main_library/index.html',
        {'all_books': obj, 'table_filter': table_filter}
    )


@login_required
def details(request, id):
    book_details = Bookshelf.objects.get(pk=id)
    return render(
        request,
        "main_library/details.html",
        {'book_details': book_details}
    )


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "świetnie. Logownie powiodło się ;).")
                return redirect('/')
            messages.error(request, "Hmmm... coś poszło nie tak.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="main_library/login.html",
                  context={"form": form})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Rejestracja powiodła się.")
            return redirect("home_page")
        messages.error(request, "Ups coś poszło nie tak.")
    form = NewUserForm
    return render(request=request, template_name="main_library/register.html", context={"register_form": form})


def logout_request(request):
    logout(request)
    messages.success(request, "wylogowałeś się.")
    return redirect('/')


def rent(request, id):
    user_id = request.user.id
    username = request.user.username

    return render(request, 'main_library/rent.html', {'user_id': user_id,
                                                      'username': username})
