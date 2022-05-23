from django.urls import path
from restaurant.views import MenuView, GalleryView

urlpatterns = [
    path('menu/', MenuView.as_view()),
    path('gallery/', GalleryView.as_view()),
]