from geopy.geocoders import Nominatim
import requests, pytemperature

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

while True:
    city = input('Mistä katsotaan lämpötilan? \n>')

    try:
        location = geolocator.geocode(city)

        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat='
                                f'{location.latitude}&lon={location.longitude}&appid=6'
                                f'e450f3e084227fa12436f7f643e5c98').json()

        main = response['main']
        result = pytemperature.k2c(main["temp"])

        print(f'Ulkona oleva lämpötila on: {round(result, 1)} °C \n')

    except:
        print("sumthin' wrong 😦, please try again \n")