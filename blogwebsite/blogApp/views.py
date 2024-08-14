from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, f"Account created successfully. Please log in.")
        return redirect('home1')

    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    return render(request, "home.html")

# def logout_user(request):
#     logout(request)
#     # messages.success(request, "You have been logged out successfully.")
#     return redirect('login') 