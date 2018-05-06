# Generated by Django 2.0.4 on 2018-05-06 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0003_auto_20180506_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='time_slot',
            field=models.TimeField(choices=[(datetime.time(9, 0), '9 AM'), (datetime.time(9, 30), '9: 30 AM'), (datetime.time(10, 0), '10 AM')]),
        ),
    ]
