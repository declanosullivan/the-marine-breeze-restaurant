from django.urls import path
from . import views
   
urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('bookings_now/', views.bookings_now, name='bookings_now'),
    path('booking_confirmed/', views.confirmation, name='booking_confirmed'),
]
