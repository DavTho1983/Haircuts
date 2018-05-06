# Generated by Django 2.0.4 on 2018-05-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('barber', models.CharField(choices=[('WD', 'William Despard'), ('CW', 'Charlotte W'), ('TH', 'Thierry Henri'), ('KB', 'Kevin Bacon'), ('KW', 'Kanye West')], max_length=2)),
                ('time_slot', models.TimeField(choices=[('9:00', '9:00'), ('9:30', '9:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'), ('18:00', '18:00')])),
                ('location', models.CharField(choices=[('CL', 'Central London'), ('NL', 'North London'), ('SL', 'South London'), ('EL', 'East London'), ('WL', 'West London')], max_length=2)),
            ],
        ),
    ]
