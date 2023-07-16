from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    books = Book.objects.filter().order_by("-created_at")
    books_per_page = 10
    paginator = Paginator(books, per_page=books_per_page)
    page_number = request.GET.get('page', 1)
    books = paginator.get_page(page_number)
    context = {
        'books': books,
        'check':paginator.count>books_per_page and books,
        'edit':False
    }
    return render(request, 'books/books_list.html', context)

@login_required(login_url='login')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.uploaded_by=request.user
            book.save()

            selected_genres = form.cleaned_data['genres']

            book.genres.set(selected_genres)
            
            book.save()
            
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'form_template.html', {'form': form,"register":"Book Upload","button_text":"Add Book"})


@login_required(login_url='login')
def edit_book(request,slug):
    book = get_object_or_404(Book, slug=slug, uploaded_by=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()

            # selected_genres = form.cleaned_data['genres']

            # book.genres.set(selected_genres)
            
            # book.save()
            
            return redirect('home')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'form_template.html', {'form': form,"register":"Book Edit","button_text":"Edit Book"})


@login_required(login_url='login')
def my_books(request):
    books = Book.objects.filter(uploaded_by=request.user).order_by("-created_at")
    books_per_page = 10
    paginator = Paginator(books, per_page=books_per_page)
    page_number = request.GET.get('page', 1)
    books = paginator.get_page(page_number)
    context = {
        'books': books,
        'check':paginator.count>books_per_page and books,
        'edit':True
    }
    return render(request, 'books/books_list.html', context)

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, "books/book_detail.html", {"book":book})