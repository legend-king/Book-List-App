from django import forms
from .models import *
from django.core.validators import FileExtensionValidator



class BookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    author = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    price = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "type":"number"}))
    publication_date = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control", "type":"date"}))

    cover_page = forms.FileField(widget=forms.FileInput(attrs={'type': 'file', 'class':"form-control"}),validators=[
            FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])
        ])

    pdf = forms.FileField(label="Book Pdf",widget=forms.FileInput(attrs={'type': 'file', 'class':"form-control"}),validators=[
            FileExtensionValidator(allowed_extensions=['pdf'])
        ])
    
    class Meta:
        model = Book
        fields = ('title', 'author', 'language', 'genres', 'description', 'price', 'publication_date', 'cover_page', 'pdf')

        widgets = {
            "language": forms.Select(attrs={"class":"form-control"})
        }