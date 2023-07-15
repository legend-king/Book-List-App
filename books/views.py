from django.shortcuts import render
from .models import Book
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    
    books = Book.objects.filter().order_by("-created_at")
    
    
    
    paginator = Paginator(books, per_page=10)
    page_number = request.GET.get('page', 1)
    books = paginator.get_page(page_number)
    context = {
        'books': books,
        'check':paginator.count>10 and books,
    }
    return render(request, 'books/books_list.html', context)