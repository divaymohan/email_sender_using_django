from django.db import models

# Create your models here.

class Users(models.Model):
    user_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)

