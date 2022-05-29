from django.shortcuts import render
from .forms import ContactForm

def menu(request):
    return render(request, 'restaurant/menu.html')

def gallery(request):
    return render(request, 'restaurant/gallery.html')    

def contact_view(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'restaurant/contact.html', context)


# from django.shortcuts import render
# from django.views.generic import TemplateView

# class RestaurantView(TemplateView):

#     template_name = "menu.html"

# class MenuView(TemplateView):

#     template_name = "menu.html"

# class GalleryView(TemplateView):
    
#     template_name = "gallery.html"

# class ContactView(TemplateView):

#     template_name = "contact.html"