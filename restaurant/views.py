from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass 
    else: 
        form = ContactForm(request)
    return render(request, 'restaurant.html', {'form': form})

