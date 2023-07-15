from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponse
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            patient = UserProfile(user=user, name=form.cleaned_data['name'],
                            phone_number=form.cleaned_data['phone_number'],
                            email=form.cleaned_data['email'],
                            gender=form.cleaned_data['gender'],)
            patient.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserProfileForm()
    return render(request, 'form_template.html', {'form': form,"register":"User Registration","button_text":"Register"})

def user_login(request):
    if request.method == 'POST':
        next = request.GET.get('next')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if next:
                    return redirect(next)
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})


@login_required(login_url='login')
def view_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    context = {'profile': profile}
    return render(request, 'users/profile.html', context)

@login_required(login_url='login')
def edit_profile(request):
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'form_template.html', {"form": form, "register":"Edit Profile","button_text":"Edit"})

def user_logout(request):
    logout(request)
    return redirect('home')