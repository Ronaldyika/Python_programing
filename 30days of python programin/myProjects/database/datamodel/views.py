from django.shortcuts import render,redirect
from .models import Detailinfo


# Create your views here.
def input(request):
    if request.method == 'POST':
        cont = Detailinfo()


        name = request.POST['name']
        school = request.POST['school']
        department = request.POST['department']
        subjects = request.POST['subjects']

        info = Detailinfo(name=name,school = school,department = department,subjects=subjects)

        info.save()
        return redirect('database')
        
    return render(request,'input.html')


def database(request):
    cont = Detailinfo.objects.all()

    return render(request,'database.html',{'data':cont})
