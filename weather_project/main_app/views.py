from django.shortcuts import render, redirect
import json
import urllib.request
import dotenv, os

from .config import open_weather_api_key

# Create your views here.
def index(request):
    if request.method == 'POST':
        location = str(request.POST['location']).capitalize()

        res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={open_weather_api_key}').read()
        
        json_data = json.loads(res)
        
        context = {
            'location': location,
            'country_code': str(json_data['sys']['country']),
            'temp': str(json_data['main']['temp']),
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity'])
        }
        
        return render(request, 'main_app/index.html', context)
    
    else:
        return render(request, 'main_app/index.html')