from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Genre, Language
from .forms import BookForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    genre_ids = request.GET.getlist('genres')
    language_ids = request.GET.getlist('languages')

    books = Book.objects.filter()

    if genre_ids:
        books = books.filter(genres__id__in=genre_ids)

    if language_ids:
        books = books.filter(language__id__in=language_ids)

    books = books.distinct().order_by("-created_at")
    context = {
        'books': books,
        'genres':Genre.objects.all(),
        'selected_genres':[int(i) for i in genre_ids],
        'languages':Language.objects.all(),
        'selected_languages':[int(i) for i in language_ids],
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
            
            return redirect('book_detail', slug)
    else:
        form = BookForm(instance=book)
    form.fields['cover_page'].widget.attrs['value'] = book.cover_page.url if book.cover_page else ''
    form.fields['pdf'].widget.attrs['value'] = book.pdf.url if book.pdf else ''
    
    return render(request, 'form_template.html', {'form': form,"register":"Book Edit","button_text":"Edit Book"})


@login_required(login_url='login')
def my_books(request):
    genre_ids = request.GET.getlist('genres')
    language_ids = request.GET.getlist('languages')

    books = Book.objects.filter(uploaded_by=request.user)

    if genre_ids:
        books = books.filter(genres__id__in=genre_ids)

    if language_ids:
        books = books.filter(language__id__in=language_ids)

    books = books.order_by("-created_at")
    
    context = {
        'books': books,
        'genres':Genre.objects.all(),
        'selected_genres':[int(i) for i in genre_ids],
        'languages':Language.objects.all(),
        'selected_languages':[int(i) for i in language_ids],
        'edit':True
    }
    return render(request, 'books/books_list.html', context)

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, "books/book_detail.html", {"book":book})