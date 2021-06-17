# weather-system
 
## Description
Web app created with Django and Python that can be used to search for weather info in specific cities using openweathermap public API and can upload weather data to MySQL or PostgreSQL databases. The current configuration uses PostgreSQL for the web app. Database weather history can be viewed in the web app as a table. 

## How to use
The code requires Python 3 which can be downloaded from https://www.python.org/downloads/ and PostgreSQL which can be downloaded at https://www.postgresql.org/download/. An API token from https://openweathermap.org/api for the "Current Weather Data" API will be required. The two python scripts, weather-info.py and weather-postgres.py, in weather-info are used to access openweathermap api and upload data to mysql and postgresql databases. The API token should be inserted into the code in the api_key variable on line 6. PostgreSQL user and database info should be inserted starting at line 27. \weatherapp\weather\utils.py contains functionality for front end and also requires the API token at line 5 in the api_key variable. The server can be started using command prompt by navigating to your \weatherapp\ directory using "cd *your directory here* and inputting "python manage.py runserver". The web page can be accessed from your localhost/weather/.

## Dependencies
The app requires the following Python libraries: requests, psycopg2, datetime.
