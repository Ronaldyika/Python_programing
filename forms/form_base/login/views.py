from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import cleint

def login(request):
    if request.method == ['POST']:
        username = request.POST['username'],
        password = request.POST['password'],
        text = request.POST['text'],

        info = cleint(username = username, password = password, text = text)

        info.save()

    return render(request,'login/template/login.html')
