from django import forms
from datetime import datetime
from django.core.exceptions import ValidationError
from .models import Tables, TableAvail


class AvailabilityForm(forms.Form):

    TableAvail.table_date = forms.DateField(required=True, widget=forms.DateInput())
    group_size = forms.IntegerField(
        required=True,
    )
