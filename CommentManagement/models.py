from django.db import models

# Create your models here.
class Comment(models.Model):
    Comment_description = models.CharField(max_length=5000)
