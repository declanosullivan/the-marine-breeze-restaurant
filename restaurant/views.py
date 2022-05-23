from django.shortcuts import render
from django.views.generic import TemplateView

class MenuView(TemplateView):
    template_name = "menu.html"

class GalleryView(TemplateView):
    template_name = "gallery.html"