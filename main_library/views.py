from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return render(request, 'main_library/home_page.html', {})

def index(request):
	return render(
		request,
		'main_library/index.html',
		{}
	)

