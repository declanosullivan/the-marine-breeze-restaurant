from datetime import datetime
from django.contrib.auth.models import User 
from tables.models import Tables
from django.db import models
import datetime



class Bookings(models.Model):
    """
    Models for bookings 
    """
    BOOKING_STATUSES = (
        ('ACT', 'ACTIVE'),
        ('COMP', 'COMPLETE'),
        ('CANC', 'CANCEL BY US'),
        ('NOSHO', 'NO_SHOW'),
    )  

    booking_ref = models.CharField(max_length=8)
    booking_date = models.DateField(default=datetime.date.today)
    booking_start = models.TimeField()
    booking_end = models.TimeField()
    booking_status = models.CharField(max_length=5, choices=BOOKING_STATUSES, default="Active")
    table =  models.ForeignKey(Tables, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE) 
    booked_by = models.CharField(max_length=10)
    booking_created = models.DateField(auto_now_add=True)
    booking_updated= models.DateTimeField(auto_now=True)

