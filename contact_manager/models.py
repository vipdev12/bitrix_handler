from django.db import models


# Create your models here.
class NamesMan(models.Model):
    name = models.CharField(max_length=255) # contact name
    phone = models.CharField(max_length=15)   # phone number

    def __str__(self):
        return f'{self.name}: {self.phone}'


class NamesWoman(models.Model):
    name = models.CharField(max_length=255)  # contact name
    phone = models.CharField(max_length=15)   # phone number

    def __str__(self):
        return f'{self.name}: {self.phone}'