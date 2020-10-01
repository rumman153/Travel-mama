from django.db import models

# Create your models here.
class Profile(models.Model):
    Profile_name = models.CharField(max_length=100)
    Profile_email = models.EmailField(max_length=100,unique=True)
    Gender = models.CharField(max_length=50,
                              choices=(('Male', 'Male'),
                                       ('Female', 'Female'),
                                       ('Other', 'Other')))

    Profile_image = models.ImageField(upload_to='images/Profile_image/', default=1)
    constitution = models.FileField(upload_to='files/constitution/', default=1)

    def __str__(self):
        return self.Profile_name


