from django.contrib import admin
from .models import Tables, TableAvail



class TableAvailAdmin(admin.ModelAdmin):
    list_display = ['id',  'table_no', 'table_date', 'table_start', 'table_end', 'is_booked']
    list_editable = ['is_booked']


# Register your models here.
admin.site.register(Tables)
admin.site.register(TableAvail, TableAvailAdmin)

