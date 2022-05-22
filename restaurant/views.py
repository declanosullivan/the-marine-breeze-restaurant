from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    """ A view to return the index page """

    return render(request, 'restaurant.html')
