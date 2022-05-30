from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'registration/login.html')    

def signup(request):
    return render(request, 'registration/signup.html')    
 
 
# Views
@login_required
def success(request):
    return render(request, "registration/success.html")

@login_required
def profile(request):
    return render(request, "registration/profile.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout(request):
    return render(request, 'registration/logout.html')   