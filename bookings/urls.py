from django.urls import path
from . import views
   
urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('book', views.bookings_now, name='bookings_now')
]