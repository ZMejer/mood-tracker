from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=35, default='')
    age = models.IntegerField(default=0)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=15, default='')
    address = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=30, default='')
    postal_code = models.CharField(max_length=6, default='')
    country = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name


#moje zadanie bedzie takie
#zrobic system logowania
#class Name to uzytkownik
#zrobic strone z resjestracją!! i logowaniem
