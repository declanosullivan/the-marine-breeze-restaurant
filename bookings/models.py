from datetime import datetime
from django.contrib.auth.models import User 
from tables.models import Tables, TableAvail
from django.db import models
import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

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




@receiver(post_save, sender=Bookings)
def update_booking(sender, instance, **kwargs):
    table = instance.table
    if instance.booking_status == "NOSHO"  or instance.booking_status == "CANC":
        TableAvail.objects.filter(table_no=table, 
                table_date=instance.booking_date, table_start=instance.booking_start,
                table_end=instance.booking_end).update(is_booked=False)

    if instance.booking_status == "ACT":
        TableAvail.objects.filter(table_no=table, 
                table_date=instance.booking_date, table_start=instance.booking_start,
                table_end=instance.booking_end).update(is_booked=True)