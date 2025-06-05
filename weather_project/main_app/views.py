from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def check_weather(request):
    location = request.POST.get('location')
    teste = 'MAS EU QUERO MUITO'
    context = {'location': location}
    return render(request, 'main_app/check_weather.html', context)