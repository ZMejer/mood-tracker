from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Name
import calendar
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

 
from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return redirect('login') 

def register(request):
    names = Name.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')
        uname = request.POST.get('uname')
        try:
            newName = Name.objects.create_user(username=uname, name=name, surname=surname, age=age, email=email, password=password, phone=phone, address=address, city=city, postal_code=postal_code, country=country)
            newName.save()
            messages.success(request, 'Rejestracja zakończona pomyślnie. Możesz się teraz zalogować.')

        except Exception as e:
            #messages.error(request, f'Błąd: {str(e)}')
            pass
            
    return render(request, "register.html")


def journal(request):
    if request.user.is_authenticated:
        return render(request, "journal.html")
    else:
        return redirect('login') 

def diet(request):
    if request.user.is_authenticated:
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
    else:
        return redirect('login') 

def loginPage(request):
    if request.method == 'POST':
        user_login = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(request, username=user_login, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, f'Witaj {user_login}. Jesteś teraz zalogowany.')
        else:
            messages.error(request, 'Hasło jest nieprawidłowe lub użytkownik nie istnieje.')
    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    messages.success(request, 'Pomyślnie wylogowano.')
    return redirect('home')

