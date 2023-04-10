from django.shortcuts import render
from .models import postmodel

# Create your views here.

def index(request):
    posts = postmodel.objects.all()
    return render(request,'blog/index.html', {'posts':posts})