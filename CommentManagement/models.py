from django.db import models
from UserManagement.models import User
from PostManagement.models import Post

# Create your models here.
class Comment(models.Model):
    Comment_description = models.TextField(max_length=5000)

    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)



