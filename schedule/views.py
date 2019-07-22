from django.shortcuts import render
from datetime import datetime, time, timedelta,date

from .models import Schedule

def index(request):
    schedule = Schedule.objects.filter(when__day=21, when__month=7, when__year=2019)
    context = {
        'schedule': schedule
    }

    return render(request, 'schedule/schedule.html', context)