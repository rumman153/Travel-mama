from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('User_Full_name','User_email','Gender','User_profile_picture','constitution')