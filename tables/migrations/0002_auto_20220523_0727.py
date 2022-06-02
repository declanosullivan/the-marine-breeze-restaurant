# Generated by Django 3.2 on 2022-05-23 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tables", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tables",
            name="table_no",
            field=models.CharField(
                choices=[
                    ("1", "ONE"),
                    ("2", "TWO"),
                    ("3", "THREE"),
                    ("4", "FOUR"),
                    ("5", "FiVE"),
                ],
                max_length=5,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="tables",
            name="table_seats",
            field=models.SmallIntegerField(
                choices=[("4", "4"), ("4", "4"), ("6", "6"), ("6", "6"), ("8", "8")]
            ),
        ),
    ]
