from django.shortcuts import render
from .models import User



def showUser(request):
    UserList = User.objects.all()
    context = {
        'user': UserList
    }
    return render(request, 'UserManagement/UserList.html', context)