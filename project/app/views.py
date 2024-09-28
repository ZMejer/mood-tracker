from django.shortcuts import render
from django.contrib import messages
from .models import Name
import calendar
from django.utils import timezone

def home(request):
    names = Name.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            newName = Name.objects.create(name=name)
        except Exception as e:
            messages.error(request, f'Błąd: {str(e)}')
    context = {'names':names}
    return render(request, "home.html", context)

def journal(request):
    return render(request, "journal.html")

def diet(request):
    now = timezone.localtime(timezone.now())
    cal = calendar.monthcalendar(now.year, now.month)
    month = now.month
    weekdays = calendar.weekheader(3).split()
    for week in cal:
        for day in range(len(week)):
            if week[day] == 0:
                week[day] = None
    context = { 'cal': cal, 'weekdays': weekdays, 'month': month }
    return render(request, "diet.html", context)