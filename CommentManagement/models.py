from django.db import models
from PostManagement.models import Post
from django.contrib.auth.models import User
#from UserManagement.models import Profile


# Create your models here.
class Comment(models.Model):
    Comment_description = models.TextField(max_length=5000)

    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.User.username



