from django.db import models

# Create your models here.
class User(models.Model):
    User_name = models.CharField(max_length=100)
    User_email = models.EmailField(max_length=100,unique=True)
    Gender = models.CharField(max_length=50,
                              choices=(('Male', 'Male'),
                                       ('Female', 'Female'),
                                       ('Other', 'Other')))

    User_profile = models.ImageField(upload_to='images/User_profile/', default=1)
    constitution = models.FileField(upload_to='files/constitution/', default=1)

    def __str__(self):
        return self.User_name


