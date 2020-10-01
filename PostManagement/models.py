from django.db import models
from django.contrib.auth.models import User
from CommentManagement.models import Comment


# Create your models here.
class Post(models.Model):
    Post_title = models.CharField(max_length=200)
    Post_location = models.CharField(max_length=50)
    Post_catagory = models.CharField(max_length=50,
                                     choices=(('Regions','Regions'),
                                              ('Popular Places', 'Popular Places'),
                                              ('Blog', 'Blog')),
                                     default='Blog')
    Post_tags = models.CharField(max_length=200)
    Post_image= models.ImageField(null='true')
    Post_description = models.TextField(max_length=100000)
    #Post_image2= models.ImageField(null='true',blank='true',default=1)
    #Post_description2 = models.TextField(max_length=100000,null='true',blank='true')
    #Post_image3 = models.ImageField(null='true',blank='true')
    #Post_description3 = models.TextField(max_length=100000, null='true',blank='true')

    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Post_title


