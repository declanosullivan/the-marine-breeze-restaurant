from django.contrib import admin
from .models import TimeSlots, OpenHours, ClosedDays

# Register your models here.
class TimeSlotsAdmin(admin.ModelAdmin):
    list_display = ("slot_start", "slot_end")


class ClosedDaysAdmin(admin.ModelAdmin):
    list_display = ("closed_date", "closed_reason")


class OpenHoursAdmin(admin.ModelAdmin):
    list_display = ("week_day", "opening_time", "closing_time")
    list_display = ("opening_time", "closing_time")


admin.site.register(OpenHours, OpenHoursAdmin)
admin.site.register(ClosedDays, ClosedDaysAdmin)
admin.site.register(TimeSlots, TimeSlotsAdmin)
