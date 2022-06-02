from django.urls import path
from . import views
from . import views as contact_views

urlpatterns = [
    path("menu/", views.menu, name="menu"),
    path("contact/", contact_views.contact_view, name="contact"),
    path("gallery/", views.gallery, name="gallery"),
]
