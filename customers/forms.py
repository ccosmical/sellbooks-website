from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

from django import forms
from django.forms.widgets import PasswordInput, TextInput

#Register a user (model form)
class CreateUserForm(UserCreationForm):
    
    class Meta:

        model = CustomUser
        fields = ['first_name', 'last_name', 'email']



# Authenticate user (model form)

class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())