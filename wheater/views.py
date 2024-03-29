from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from .apikeys import key
def index(request):

    url = key

    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : round((city_weather['main']['temp']-32)/1.8, 2),
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'wheater/index.html', context)
