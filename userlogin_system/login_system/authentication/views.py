from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')


def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        secondname = request.POST['secondname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(firstname, email,pass1)

        myuser.save()
        messages.success(request,'your account was created successfully')
        return redirect('signin')




    return render(request, 'authentication/signup.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']

        user = authenticate(email = email, password = pass1)
        if user is not None:
            login(request,user)
            return render(request,'authentication/index.html')
        else:
            messages.error(request,'bad issues')
            return redirect('home')
    return render(request, 'authentication/index.html' )


def signout(request):
    logout(request)
    messages.success(request,'logged out success')
    return redirect('home')