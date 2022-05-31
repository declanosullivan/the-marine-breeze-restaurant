from django.shortcuts import render
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from bookings.models import Bookings

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')

def login(request):
    """ A view to return the login page """
    return render(request, 'registration/login.html')    

def signup(request):
    """ A view to return the signup page """
    return render(request, 'registration/signup.html')    
 
 
# Views
@login_required
def success(request):
    """ A view to return the success page """
    return render(request, "registration/success.html")

def profile(request):
    """ 
    Display loggin user profile showing their bookings
    """
    bookingsresults = Bookings.objects.filter(customer=request.user)
    return render(request, "registration/profile.html", {"userbookings": bookingsresults})

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

def logout_view(request):
    logout(request)
    return render(request, 'home/index.html')   