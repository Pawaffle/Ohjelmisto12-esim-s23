import mysql.connector
from geopy.distance import geodesic

user = 'username'  # input('username \n>')
password = 'password'  # input('password \n>')

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user=user,
         password=password,
         autocommit=True
         )

'''
########################################################################################################
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. Ohjelma ilmoittaa lentokenttien 
välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin. 
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/. Asenna kirjasto 
valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun.
########################################################################################################
'''
#select latitude_deg, longitude_deg from airport where ident = 'EFHK';

def get_location_of_airport(code):
    cursor = yhteys.cursor()
    cursor.execute(f"select latitude_deg, longitude_deg from airport where ident = '{code}'")
    result = cursor.fetchall()
    if result:     # jos ei ole lopputulosta = none = false
        return result
    else:
        return 'Ei löydyy'


ICAO = input('Anna lentokentän ICAO-koodi: ')
location1 = get_location_of_airport(ICAO)
ICAO = input('Anna toisen lentokentän ICAO-koodi: ')
location2 = get_location_of_airport(ICAO)

distance = geodesic(location1, location2).kilometers
print(f'\n   Lentokenttien etäisyys on: {distance:.2f} km.')