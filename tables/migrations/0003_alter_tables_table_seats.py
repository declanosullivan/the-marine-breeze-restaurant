# Generated by Django 3.2 on 2022-05-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_auto_20220523_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tables',
            name='table_seats',
            field=models.SmallIntegerField(choices=[(4, 4), (4, 4), (6, 6), (6, 6), (8, 8)]),
        ),
    ]
