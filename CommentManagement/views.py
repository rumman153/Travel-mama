from django.shortcuts import render
from .models import Comment



def showComment(request):
    commentList = Comment.objects.all()
    context = {
        'comment': commentList
    }
    return render(request, 'CommentManagement/CommentList.html', context)