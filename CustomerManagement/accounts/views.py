from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.



def customer(request):
    return render(request,'accounts/customer.html')

def products(request):
    return render(request,'accounts/products.html')
def dashbord(request):
    return render(request,'accounts/dashbord.html')