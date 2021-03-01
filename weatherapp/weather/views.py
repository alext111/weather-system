from django.shortcuts import render
from weather.models import Info
from weather.utils import getWeather

def weather_info(request):
    info_objs = Info.objects.all()

    context = {
        'info_data': info_objs
    }

    return render(request, 'weather_data.html', context)

def search(request):
    if request.method == 'POST':
        city_name = request.POST.get("city_name", None)
        state_code = request.POST.get("state_code", None)
        country_code = request.POST.get("country_code", None)
        data = getWeather(str(city_name),str(state_code),str(country_code))

        # return user to required page
        return render(request, 'weather_search_result.html', {'search_data': data})

    return render(request, 'weather_search.html')

def main(request):
    return render(request, 'main.html', None)

# Create your views here.
