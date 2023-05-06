from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .models import User
#from django.contrib.auth.models import User
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method =='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password != password1:
            messages.error(request,'bad request')
            return render(request,'signup.html')
        else:
            if User.objects.filter(username = username).exists:
                messages.info(request,'username already taken ')
                return redirect('signup')
            else:
                user = User.objects.create(username= username,password=password,firstname=firstname,email=email)
                user.save()
                return redirect('signin')
    return render(request,'signup.html')

def signin(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['pass1']

        user = authenticate(username = username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            
            return render(request,'signin.html')

    return render(request,'signin.html')