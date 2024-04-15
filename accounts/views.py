from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request,'signup.html',{'form':form})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = CustomUser.objects.get(email=email)
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            print("Authentication failed!")
            # Handle invalid login
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')