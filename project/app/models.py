from django.db import models
from django.contrib.auth.models import AbstractUser

class Name(AbstractUser):
    name=models.CharField(default='', max_length=30)
    surname=models.CharField(default='', max_length=30)
    age=models.IntegerField(default=0)
    calorie_goal = models.IntegerField(default=2000)
    email=models.CharField(default='', max_length=30)
    phone=models.IntegerField(default=0)
    address=models.CharField(default='', max_length=30)
    city=models.CharField(default='', max_length=30)
    postal_code=models.CharField(default='', max_length=30)
    country=models.CharField(default='', max_length=30)
    def __str__(self):
        return self.name
