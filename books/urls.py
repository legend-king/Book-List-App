from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_books', views.my_books, name='my_books'),
    path('add_book', views.add_book, name="add_book"),
    path('edit_book/<str:slug>', views.edit_book, name="edit_book"),
    path('book_detail/<str:slug>', views.book_detail, name="book_detail"),
]