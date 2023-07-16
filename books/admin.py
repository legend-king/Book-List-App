from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title','author', 'language', 'publication_date','uploaded_by', 'created_at')
    list_filter = ('genres', 'language', 'price')
    search_fields = ('title', 'author', 'description')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields = ('name',)

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields = ('name',)