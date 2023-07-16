from django.contrib import admin
from .models import UserProfile
# Register your models here.
@admin.register(UserProfile)
class UserProfuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'gender')
    list_filter = ('gender',)
    search_fields=('name', 'eamil', 'mobile')