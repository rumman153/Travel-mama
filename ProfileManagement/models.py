from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    User_Full_name = models.CharField(max_length=100)
    User_email = models.EmailField(max_length=100, unique=True)
    Gender = models.CharField(max_length=50,
                              choices=(('Male', 'Male'),
                                       ('Female', 'Female'),
                                       ('Other', 'Other')))

    User_profile_picture = models.ImageField(upload_to='images/User_profile_picture/', default=1)
    constitution = models.FileField(upload_to='files/constitution/', default=1)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
