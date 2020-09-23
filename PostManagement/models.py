from django.db import models
from UserManagement.models import User

# Create your models here.
class Post(models.Model):
    Post_title = models.CharField(max_length=200)
    Post_location = models.CharField(max_length=50)
    Post_catagory = models.CharField(max_length=50)
    Post_tags = models.CharField(max_length=200)
    Post_description = models.TextField(max_length=100000)

    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.Post_title


