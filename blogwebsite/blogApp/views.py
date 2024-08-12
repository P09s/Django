from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

def indexV(request):
    return render(request, "index.html")

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('/admin/')  # Redirect to admin panel
                else:
                    return redirect('home1')  # Redirect to the 'home1' view
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_type = request.POST.get('user_type')  # Get the user type from the form
        if form.is_valid():
            user = form.save(commit=False)
            if user_type == 'admin':
                user.is_staff = True  # Assign staff status for admin-like users
            # Save the user
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}. Please log in.")
            return redirect('home1')
        else:
            messages.error(request, "Failed to create account. Please correct the errors below.")
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    return render(request, "home.html")