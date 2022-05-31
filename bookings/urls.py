from django.urls import path
from . import views
   
urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('create_availability/', views.create_availability, name='create_availability'),
    path('create_availability_daily/', views.create_availability_daily, name='create_availability_daily'),
    path('bookings_now/', views.bookings_now, name='bookings_now'),
    path('<int:booking_id>/booking_cancel', views.booking_cancel, name='booking_cancel'),
]
