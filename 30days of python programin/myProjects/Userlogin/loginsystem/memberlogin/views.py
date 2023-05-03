from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Registeration

# Create your views here.
def home(request):
    users = Registeration.objects.all()
    context = {
        'info':users
    }
    return render(request,'home.html',context)

def register(request):
    #user = Registeration()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            new_user = Registeration(name=name,email=email,password = password)
            

            new_user.save()
            messages.info(request,'information saved succesfully')

            return redirect('login')
        else:
            messages.info(request,'your password has to be thesame')
            return redirect('register')



    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        user = auth.authenticate(email=email,password=password1)

        if user is not None:
            auth.login(request,user)
            return redirect(request,'home')
    return render(request,'login.html')