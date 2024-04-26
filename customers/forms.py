from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 


from django import forms
from django.forms.widgets import PasswordInput, TextInput

#Register a user (model form)
class CreateUserForm(UserCreationForm):
    
    class Meta:

        model = User
        fields = ['username','email', 'password1', 'password2']



# Authenticate user (model form)

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())