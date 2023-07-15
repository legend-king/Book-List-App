from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=[("m", "Male"), ('f', "Female"), ('o',"other")], null=True, blank=True)

    def __str__(self):
        return str(self.user)