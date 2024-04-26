from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.decorators import login_required

# Authentication model functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout   

# Create your views here.

def homepage(request):
    pass



def register(request):
    
    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    context = {'registerform': form}

    return render(request, 'templates/register.html', context=context)





def login(request):
    form = LoginForm

    if request.method == "POST":
        
        form = LoginForm(request, data= request.POST)

        if form.is_valid:

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')
            
    context = {'loginform':form}

    return render(request, 'templates/login.html', context=context)


def logout(request):

    auth.logout(request)
    return redirect('login')  # To use redirect, I need to set a name for urls in urls.py file



@login_required(login_url='login')
def dashboard(request):

    return render(request, 'templates/dashboard.html')