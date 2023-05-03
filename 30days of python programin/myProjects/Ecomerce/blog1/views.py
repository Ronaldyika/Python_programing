from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def jewellery(request):
    return render(request,'jewellery.html')
def fashion(request):
    return render(request,'fashion.html')

def electronic(request):
    return render(request,'electronic.html')