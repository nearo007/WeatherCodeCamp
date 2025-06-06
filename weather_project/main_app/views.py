from django.shortcuts import render, redirect
import json
import urllib.request
from urllib.parse import quote

from .config import open_weather_api_key

# Create your views here.
def index(request):
    if request.method == 'POST':
        location = str(request.POST['location']).capitalize()
        location_formated = quote(location)

        res = urllib.request.urlopen(f'http://api.openweathermap.org/data/2.5/weather?q={location_formated}&appid={open_weather_api_key}').read()
        
        json_data = json.loads(res)
        
        location_words = location.split(' ')
        
        for word in location_words:
            location = location.replace(word, word.capitalize())

        context = {
            'location': location,
            'country_code': str(json_data['sys']['country']),
            'temp': str(int((json_data['main']['temp']) - 273.15)),
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity'])
        }
        
        return render(request, 'main_app/index.html', context)
    
    else:
        return render(request, 'main_app/index.html')