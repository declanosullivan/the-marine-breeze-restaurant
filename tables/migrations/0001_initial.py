# Generated by Django 4.0.4 on 2022-05-19 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tables",
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
                (
                    "table_no",
                    models.CharField(
                        choices=[
                            ("1", "ONE"),
                            ("2", "TWO"),
                            ("3", "THREE"),
                            ("4", "FOUR"),
                        ],
                        max_length=5,
                        unique=True,
                    ),
                ),
                ("table_seats", models.SmallIntegerField()),
                (
                    "table_status",
                    models.CharField(
                        choices=[("ACT", "ACTIVE"), ("OFF", "OFFLINE")],
                        default="Active",
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TableAvail",
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
                ("table_date", models.DateField()),
                ("table_start", models.TimeField()),
                ("table_end", models.TimeField()),
                ("is_booked", models.BooleanField(default=False)),
                (
                    "table_no",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="tables.tables"
                    ),
                ),
            ],
        ),
    ]
