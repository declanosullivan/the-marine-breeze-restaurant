from django.contrib import admin
from .models import Bookings

# Register your models here.
class BookingsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "booking_ref",
        "booking_date",
        "booking_start",
        "booking_end",
        "booking_status",
        "table",
        "customer",
        "booked_by",
        "booking_created",
        "booking_updated",
    ]
    list_editable = ["booking_status"]


# Register your models here.
admin.site.register(Bookings, BookingsAdmin)
