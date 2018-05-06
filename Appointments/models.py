from django.db import models
from datetime import time

class Barber(models.Model):

    BARBERS = (
        ('KK', 'Kim Kardashian'),
        ('CJ', 'Caitlin Jenner'),
        ('KW', 'Kanye West')
    )

    LOCATION = (
        ('CL', 'Central London'),
        ('NL', 'North London'),
        ('SL', 'South London'),
        ('EL', 'East London'),
        ('WL', 'West London'),
    )

    name = models.CharField(max_length=2, choices=BARBERS)
    location = models.CharField(max_length=2, choices=LOCATION)

    def __str__(self):
        return self.name

class Date(models.Model):

    date = models.DateField()
    name = models.ForeignKey(Barber, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

class Times(models.Model):

    TIME_SLOTS = (
        (time(9, 00, 00), u'9 AM'),
        (time(9, 30, 00), u'9: 30 AM'),
        (time(10, 00, 00), u'10 AM'),
    )

    time_slot = models.TimeField(choices = TIME_SLOTS)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
