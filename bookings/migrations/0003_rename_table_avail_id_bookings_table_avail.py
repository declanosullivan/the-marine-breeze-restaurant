# Generated by Django 3.2 on 2022-05-31 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20220531_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='table_avail_id',
            new_name='table_avail',
        ),
    ]