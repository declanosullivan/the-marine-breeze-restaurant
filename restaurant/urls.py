from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
]
