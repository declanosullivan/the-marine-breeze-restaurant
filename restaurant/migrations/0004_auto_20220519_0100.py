# Generated by Django 3.2 on 2022-05-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_closeddays_closed_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslots',
            name='slot_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='timeslots',
            name='slot_start',
            field=models.DateField(),
        ),
    ]
