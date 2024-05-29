from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import signupform

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')  
        password = request.POST.get('password') 

        if username and password:  
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have logged in successfully")
                return redirect('home')
            else:
                messages.error(request, "There was an error logging in. Please try again.")
                return redirect('home')
        else:
            messages.error(request, "Username and password are required.")
            return redirect('home')
    
    return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out successfully")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('home')
    else:
        form = signupform()
    return render(request, 'register.html', {'form': form})