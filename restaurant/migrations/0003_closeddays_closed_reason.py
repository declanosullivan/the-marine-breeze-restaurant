# Generated by Django 3.2 on 2022-05-18 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_auto_20220518_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='closeddays',
            name='closed_reason',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]