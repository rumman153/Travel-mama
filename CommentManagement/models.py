from django.db import models
from ProfileManagement.models import Profile
from PostManagement.models import Post

# Create your models here.
class Comment(models.Model):
    Comment_description = models.TextField(max_length=5000)

    Profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    Post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.User.User_name



