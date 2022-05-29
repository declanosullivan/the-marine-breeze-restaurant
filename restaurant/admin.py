from django.contrib import admin
from .models import TimeSlots, OpenHours, ClosedDays

# Register your models here.
admin.site.register(OpenHours)
admin.site.register(ClosedDays)


class TimeSlotsAdmin(admin.ModelAdmin):
    list_display = ("slot_start", "slot_end")


admin.site.register(TimeSlots, TimeSlotsAdmin)
