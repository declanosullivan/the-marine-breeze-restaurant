# Generated by Django 4.0.4 on 2022-05-19 19:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tables", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bookings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("booking_ref", models.CharField(max_length=8)),
                ("booking_date", models.DateField(default=datetime.date.today)),
                ("booking_start", models.TimeField()),
                ("booking_end", models.TimeField()),
                (
                    "booking_status",
                    models.CharField(
                        choices=[
                            ("ACT", "ACTIVE"),
                            ("COMP", "COMPLETE"),
                            ("CANC", "CANCEL BY US"),
                            ("NOSHO", "NO_SHOW"),
                        ],
                        default="Active",
                        max_length=5,
                    ),
                ),
                ("booked_by", models.CharField(max_length=10)),
                ("booking_created", models.DateField(auto_now_add=True)),
                ("booking_updated", models.DateTimeField(auto_now=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tables.tables"
                    ),
                ),
            ],
        ),
    ]
