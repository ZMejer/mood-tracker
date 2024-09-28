from django.shortcuts import render
from django.contrib import messages
from .models import Name

 
def home(request):
    
    return render(request, "home.html", context)


def register(request):
    names = Name.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')
        
        try:
            messages.success(request, f'Użytkownik {name} {surname} został dodany do bazy danych')
            newName = Name.objects.create(name=name, surname=surname, age=age, email=email, password=password, password2=password2, phone=phone, address=address, city=city, postal_code=postal_code, country=country)
        except Exception as e:
            messages.error(request, f'Błąd: {str(e)}')
            
    context = {'names':names}
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")