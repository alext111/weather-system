import requests
from datetime import date

#api key and city id for openweathermapapi
api_key = '9d899b36cc540f63dae387657f3b1c1a'

def getWeather(city_name):
    # obtains api data in json format
    weatherData = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key)
    weatherData = weatherData.json()

    # convert temperatures from kelvin to fahrenheit
    tempMaxFahrenheit = (weatherData['main']['temp_max'] - 273.15) * 1.8 + 32
    tempMinFahrenheit = (weatherData['main']['temp_min'] - 273.15) * 1.8 + 32
    tempMaxFahrenheit = round(tempMaxFahrenheit, 2)
    tempMinFahrenheit = round(tempMinFahrenheit, 2)

    # list of desired values for database storage
    values = [date.today().strftime('%Y-%m-%d'), weatherData['name'], weatherData['weather'][0]['main'],
              tempMaxFahrenheit, tempMinFahrenheit, weatherData['main']['humidity']]

    return values