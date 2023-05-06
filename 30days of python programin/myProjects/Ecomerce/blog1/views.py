from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    details = collection.objects.all()
    items = electronics.objects.all()
    context = {
        'details':details,
        'items':items
    }

    return render(request,'index.html',context)
def jewellery(request):
    return render(request,'jewellery.html')
def fashion(request):
    details = collection.objects.all()
    context = {
        'details':details
    }
    return render(request,'fashion.html',context)

def electronic(request):
    return render(request,'electronic.html')