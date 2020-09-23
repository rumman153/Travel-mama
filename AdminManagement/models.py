from django.db import models

# Create your models here.
class Admin(models.Model):
    Admin_name = models.CharField(max_length=100)
    Admin_email = models.EmailField(max_length=100,unique=True)
    Admin_contact = models.IntegerField(unique=True)

    def __str__(self):
        return self.Admin_name
