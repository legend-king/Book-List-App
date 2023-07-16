from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserProfileForm(UserCreationForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mobile = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', "type":"email"}))
    gender = forms.ChoiceField(
        choices=[('m', "Male"), ("f", "Female"), ("o", "Other")],
        widget=forms.RadioSelect
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        
        model = User
        fields = ( 'name', 'username','mobile', 'email', 'gender', 'password1', 'password2')


class ProfileEditForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    mobile = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', "type":"email"}))
    gender = forms.ChoiceField(
        choices=[('m', "Male"), ("f", "Female"), ("o", "Other")],
        widget=forms.RadioSelect
    )
    class Meta:
        model = UserProfile
        fields = ('name', 'mobile', 'email', 'gender')