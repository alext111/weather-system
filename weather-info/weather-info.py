# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
import pymysql
from datetime import date
import schedule
import time

#api key and city id for openweathermapapi
api_key = ''
city_id = '4787117'

#function to get weather info from api
def getWeather():
    # database connection
    db = pymysql.connect('localhost', 'testuser', 'testpw', 'testdb')
    cursor = db.cursor()

    #obtains api data in json format
    weatherData = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+city_id+'&appid='+api_key)
    weatherData = weatherData.json()

    #convert temperatures from kelvin to fahrenheit
    tempMaxFahrenheit = (weatherData['main']['temp_max'] - 273.15) * 1.8 + 32
    tempMinFahrenheit = (weatherData['main']['temp_min'] - 273.15) * 1.8 + 32

    #list of desired values for database storage
    values = [date.today().strftime('%Y-%m-%d'),weatherData['name'],weatherData['weather'][0]['main'],tempMaxFahrenheit,tempMinFahrenheit,weatherData['main']['humidity']]
    sql = """INSERT INTO weather (day, city, description, temp_max, temp_min, humidity) VALUES (%s, %s, %s, %s, %s, %s)"""

    #try sending info to database, rollback if error occurs
    try:
        cursor.execute(sql, values)
        db.commit()
    except:
        db.rollback()

    db.close()

'''
#run weather function everyday at 9pm, must launch python program
schedule.every().day.at("21:00").do(getWeather)
while True:
    schedule.run_pending()
    time.sleep(1)
'''

#call weather function, used for bat file version
getWeather()