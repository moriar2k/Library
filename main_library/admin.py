from django.contrib import admin
from .models import *

class CustomBookManage(admin.ModelAdmin):
	list_display = ( 'title', 'author', 'kind', 'epoch', 'genre', 'quantity')
	search_fields = ('title', 'author', 'quantity')
	list_filter = ('kind', 'author', 'epoch')

	filter_horizontal = ()
	fieldsets = ()



admin.site.register(Bookshelf, CustomBookManage)

# Register your models here.
