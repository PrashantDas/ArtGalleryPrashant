from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormRegisterArtist(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']




class FormLoginArtist(forms.Form):
    email    = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
