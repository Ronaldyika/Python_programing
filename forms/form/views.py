from django.shortcuts import render
from .models import details

# Create your views here.
from  django.http import HttpResponse
def form(request):
        if request.method =='POST':
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            new_info = details(name = name,email = email, password = password)

            print(name, email,password)
            
            new_info.save()
        return render(request,'forms/templates/forms.html')
