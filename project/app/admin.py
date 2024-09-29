from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Name, Diet

admin.site.register(Name)
admin.site.register(Diet)