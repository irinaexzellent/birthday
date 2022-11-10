from calendar import HTMLCalendar
from datetime import datetime

from django.shortcuts import render

from .models import User


def index(request):
    page_obj = User.objects.filter(dob__day=datetime.now().date().day, dob__month=datetime.now().date().month)
    template = 'birthday_show/index.html'
    year = int(datetime.now().date().year)
    month = int(datetime.now().date().month)
    now = datetime.now()
    time = now.strftime('%I:%M:%S %p')
    cal = HTMLCalendar().formatmonth(year, month)
    context = {
        'page_obj': page_obj,
        'year': year,
        'month': month,
        'cal': cal,
        'time': time,
    }
    return render(request, template, context)

