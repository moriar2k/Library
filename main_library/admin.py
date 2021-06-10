from django.contrib import admin
from .models import *


class CustomBookManage(admin.ModelAdmin):
    list_display = ('title', 'author', 'kind', 'epoch', 'genre', 'quantity')
    search_fields = ('title', 'author', 'quantity')
    list_filter = ('kind', 'author', 'epoch')

    filter_horizontal = ()
    fieldsets = ()


class CustomRentList(admin.ModelAdmin):
    list_display = ('book_id', 'user_id', 'planned_date_of_return')
    search_fields = ('user_id', 'book_id')
    list_filter = ('user_id', 'book_id')

    filter_horizontal = ()
    fieldsets = ()


admin.site.register(Bookshelf, CustomBookManage)
admin.site.register(RentalList, CustomRentList)

# Register your models here.
