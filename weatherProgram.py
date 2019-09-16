from datetime import datetime
import requests
import pytemperature
import pprint

#initialize time/date
now = datetime.now()

#print heading
print("ISQA 3900 Open Weather API")

#print formatted date
print(now.strftime("%A, %d %B, %Y"))

choice = "y"
#while user enters y it will run again, else it will exit
while choice.lower() == "y":
    city = input("\nEnter city:     ")
    print("Use ISO letter country code like: https://countrycode.org/")
    country = input("Enter country code:     ")

    #api cradentials
    api_start = 'https://api.openweathermap.org/data/2.5/weather?q='
    api_key = '&appid=910696573d411e89ac1eb5cced2835d9'
    url = api_start + city + ',' + country + api_key

    #data that is returned from api
    json_data = requests.get(url).json()

    #check if values entered are correct, if not, prompt them again
    if json_data['cod'] != '404':
        #extract data points from json
        weather_description = json_data['weather'][0]['description']
        current_temp_fahrenheit = pytemperature.k2f(json_data['main']['temp'])
        current_low_temp_fahrenheit = pytemperature.k2f(json_data['main']['temp_min'])
        current_high_temp_fahrenheit = pytemperature.k2f(json_data['main']['temp_max'])
        current_pressure = json_data['main']['pressure']
        current_humidity = json_data['main']['humidity']

        #print results
        print("Current conditions:  ", weather_description)
        print("Current Temperature in Fahrenheit:  ", current_temp_fahrenheit)
        print("Current pressure in inHg:  ", current_pressure)
        print("Current % humidity:  ", current_humidity)
        print("Expected low temperature in Fahrenheit:  ", current_low_temp_fahrenheit)
        print("Expected high temperature in Fahrenheit:  ", current_high_temp_fahrenheit)

        choice = input("Continue (y/n)?: ")

    else:
        print("\nIncorrect value entered\n")
        choice = input("Try again (y/n)?: ")

print('\nBye')