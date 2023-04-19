from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')


def weather(request):
    city = request.GET.get('city')
    print(city)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=af0d27ada9e27549bbfcbd6265bd9704'#enter apikey after the last =
    resp = requests.get(url)
    response = resp.json()
    temperature = response['main']['temp']
    #bg_color = ['bg-primary','bg-secondary','bg-warming','bg-success','bg-info']
    context = {'temperature':temperature, 'city':city }
    return render(request,'weather.html',context)


