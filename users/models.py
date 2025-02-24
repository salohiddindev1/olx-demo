from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import BASE

# Create your models here.
class User(AbstractUser,BASE):
    photo = models.ImageField(upload_to='users/photo')
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=20,blank=True, null=True)
    birth_date  = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255 ,null=True, blank=True)