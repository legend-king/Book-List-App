from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
    publication_date = models.DateField()
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    cover_page = models.ImageField(upload_to='cover_page', null=True, blank=True)
    pdf = models.FileField(upload_to='books')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    def save(self, *args, **kwargs):
        if not self.slug or Book.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Book.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.title