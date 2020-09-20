from django.shortcuts import render
from .models import Admin



def showAdmin(request):
    adminList = Admin.objects.all()
    context = {
        'admin': adminList
    }
    return render(request, 'AdminManagement/AdminList.html', context)