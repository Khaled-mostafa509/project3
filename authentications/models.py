from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    
  is_person = models.BooleanField(default=False)
  is_company = models.BooleanField(default=False)

class Person(models.Model):
    user = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)

class Company(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    tax_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)