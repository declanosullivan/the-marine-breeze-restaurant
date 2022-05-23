from django.shortcuts import render

def menu(request):
    return render(request, 'restaurant/menu.html')

def contact(request):
    return render(request, 'restaurant/contact.html')    

def gallery(request):
    return render(request, 'restaurant/gallery.html')    



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