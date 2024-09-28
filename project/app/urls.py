from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("journal", views.journal, name="journal"),
    path("diet", views.diet, name="diet"),
    path("register", views.register, name="register"),
]