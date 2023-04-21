from django.shortcuts import render,redirect

# Create your views here.
from .models import User


def index(request):
    users = User.objects.all()
    users.save()
    context = {'users': users}

    return render(request,'index.html',context)

def create(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        users =  User(username = username, email = email)

        users.save()
        return redirect('index')
    else:
        return render(request,'create.html')

def update(request,pk):

    users = User.objects.get(pk=pk)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        users.username
        users.email

        users.save()

        return redirect('index')
    else:
        context = {'users': users}
        return render(request,'update.html',context)

def delete(request,pk):
    users = User.objects.get(pk)

    users.delete()
    return redirect('index')