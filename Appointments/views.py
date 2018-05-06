from django.shortcuts import render, redirect
from .models import Barber, Date, Times

def schedule(request):
    barber = Barber.objects.all()
    return render(request, 'schedule.html', {'barber': barber})

def appointments(request, id):
    barb = Barber.objects.get(id=id)
    dates = barb.date_set.all()
    return render(request, 'appointments.html', {'dates': dates, 'barb': barb})

def times(request, id):
    date = Date.objects.get(id=id)
    times = date.times_set.all()
    return render(request, 'timeslots.html', {'date': date, 'times': times})
