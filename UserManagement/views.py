from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def showUser(request):
    UserList = User.objects.all()
    context = {
        'User': UserList
    }
    return render(request, 'UserManagement/UserList.html', context)

def registration(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    context = {
        'form' : form

    }
    return render(request, 'UserManagement/registration.html', context)

@login_required
def insertUser(request):
    message = ""
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST,request.FILES)
        message = "you are wrong!!!!!"
        if form.is_valid():
            form.save()
            message = "Success..."
            form = UserForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'UserManagement/insertUser.html', context)
