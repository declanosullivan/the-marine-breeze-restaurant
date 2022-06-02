# Generated by Django 3.2 on 2022-05-31 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_alter_tables_table_seats'),
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='table_avail_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tables.tableavail'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookings',
            name='booking_status',
            field=models.CharField(choices=[('ACT', 'ACTIVE'), ('COMP', 'COMPLETE'), ('CANC', 'CANCEL BY US'), ('NOSHO', 'NO_SHOW')], default='Active', max_length=20),
        ),
    ]