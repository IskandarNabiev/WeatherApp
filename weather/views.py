import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    appid = 'e26841938e6ab55dfd13e3fcbb783194'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid


    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()



    # city = 'London'

    # print(res.text)

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
