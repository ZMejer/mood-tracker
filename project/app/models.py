from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=35, default='')
    def __str__(self):
        return self.name
