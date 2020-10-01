from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



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
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        message = "you are wrong!!!!!"
        if form.is_valid():
            form.save()
            message = "Success..."
            form = ProfileForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request,'UserManagement/insertUser.html', context)

@login_required
def showProfile(request):
    try:
        ProfileList = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = "Please complete your profile to view"

    context = {
        'Profile': Profile
    }
    return render(request, 'UserManagement/viewProfile.html', context)

@login_required
def createProfile(request):
    message = ""
    form =ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        message = "you are wrong!!!!!"
        if form.is_valid():

            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            message = "Profile Update Successfully..."
            form = ProfileForm()

    context = {
        'form' : form,
        'message' : message
    }
    return render(request, 'UserManagement/createProfile.html', context)
