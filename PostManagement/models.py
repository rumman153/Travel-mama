
from django.db import models

# Create your models here.
class Post(models.Model):
    Post_title = models.CharField(max_length=200)
    Post_location = models.CharField(max_length=50)
    Post_catagory = models.CharField(max_length=50)
    Post_tags = models.CharField(max_length=200)
    Post_description = models.TextField(max_length=100000)

