from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from .models import Bookshelf
from django.contrib.auth.models import User
from .filters import UserFilter
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate


# Create your views here.
def home_page(request):
    return render(request, 'main_library/home_page.html', {})


def index(request):
    obj = Bookshelf.objects.values('title', 'author', 'genre', 'kind', 'epoch', 'quantity', 'id')
    table_filter = UserFilter(request.GET, queryset=obj)
    # obj = myFilter.qs
    return render(
        request,
        'main_library/index.html',
        {'all_books': obj, 'table_filter': table_filter}
    )


def wypozycz(request, id):
    return render(
        request,
        "main_library/wypozycz.html",
        {}
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
                return redirect('/')
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
