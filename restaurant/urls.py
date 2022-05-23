from django.urls import path
from restaurant.views import RestaurantView, MenuView, GalleryView, ContactView

urlpatterns = [
    path('', RestaurantView.as_view(), name='restaurant'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('contact/', ContactView.as_view(), name='contact'),
]