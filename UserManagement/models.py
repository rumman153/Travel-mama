from django.db import models

# Create your models here.
class User(models.Model):
    User_name = models.CharField(max_length=100)
    User_email = models.EmailField(max_length=100,unique=True)
    Gender = models.CharField(max_length=50)

