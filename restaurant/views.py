from django.shortcuts import render
from .forms import ContactForm


def menu(request):
    return render(request, "restaurant/menu.html")


def gallery(request):
    return render(request, "restaurant/gallery.html")


def contact_view(request):
    form = ContactForm()
    context = {"form": form}
    return render(request, "restaurant/contact.html", context)
