import requests
from datetime import date

#api key and city id for openweathermapapi
api_key = '9d899b36cc540f63dae387657f3b1c1a'

def getWeather(city_name,state_code,country_code):
    # obtains api data in json format
    if country_code != "" and state_code != "":
        weatherData = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + ',' + state_code + ',' + country_code + '&appid=' + api_key)
    elif state_code != "":
        weatherData = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + ',' + state_code + '&appid=' + api_key)
    elif country_code != "":
        weatherData = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + ',' + country_code + '&appid=' + api_key)
    else:
        weatherData = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key)
    weatherData = weatherData.json()
    print(weatherData)
    # convert temperatures from kelvin to fahrenheit
    tempMaxFahrenheit = (weatherData['main']['temp_max'] - 273.15) * 1.8 + 32
    tempMinFahrenheit = (weatherData['main']['temp_min'] - 273.15) * 1.8 + 32
    tempMaxFahrenheit = round(tempMaxFahrenheit, 2)
    tempMinFahrenheit = round(tempMinFahrenheit, 2)

    # list of desired values for database storage
    values = [date.today().strftime('%Y-%m-%d'), weatherData['name'], weatherData['weather'][0]['main'],
              tempMaxFahrenheit, tempMinFahrenheit, weatherData['main']['humidity']]

    return values