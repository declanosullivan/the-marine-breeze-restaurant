from django.db import models


class TimeSlots(models.Model):
    """
    Models for duration of time a table can be available for
    """
    slot_start = models.TimeField()
    slot_end = models.TimeField()


class OpenHours(models.Model):
    """
    Models for hours restaurant open and slots tables are available
    """
    WEEKDAYS = (
        ('SUN', 'SUNDAY'),
        ('MON', 'MONDAY'),
        ('TUE', 'TUESDAY'),
        ('WED', 'WEDNESDAY'),
        ('THU', 'THURSDAY'),
        ('FRI', 'FRIDAY'),
        ('SAT', 'SATURDAY'),
    )

    week_day = models.CharField(max_length=7, unique=True, choices=WEEKDAYS)
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.week_day}: Open at {self.opening_time} and closed at {self.closing_time}"



class ClosedDays(models.Model):
    """
    Models for days closed due to holidays or operational issues
    """
    closed_date = models.DateField()
    closed_reason = models.TextField()

    def __str__(self):
        return self.closed_date

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=25, blank=True)
    message = models.TextField(blank=True)