# Generated by Django 2.0.4 on 2018-05-06 18:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0005_auto_20180506_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Times',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_slot', models.TimeField(choices=[(datetime.time(9, 0), '9 AM'), (datetime.time(9, 30), '9: 30 AM'), (datetime.time(10, 0), '10 AM')])),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Appointments.Date')),
            ],
        ),
    ]
