from django.shortcuts import render
from django.contrib import messages
from .models import Name

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