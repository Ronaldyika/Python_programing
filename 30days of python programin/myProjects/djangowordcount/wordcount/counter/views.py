from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse

def index(request):


    return render(request,'index.html')
def index2(request):
        if request.method == 'POST':
            text = request.POST['text']
            word = len(text.split())
            print(word)

            context = { 
            'word':word
            }
        return render(request,'index2.html',context)

