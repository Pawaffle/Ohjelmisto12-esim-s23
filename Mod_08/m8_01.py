import mysql.connector

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
###################################################################################################
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia 
vastaavan LENTOKENTÄN NIMEN ja sen SIJAINTIKUNNEN kurssilla käytettävästä lentokenttätietokannasta. 
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
###################################################################################################
'''

# select name, municipality from airport where ident = 'xxxx';

def get_airport_by_icao_code(ICAO_code):
    cursor = yhteys.cursor()
    cursor.execute(f"select name, municipality from airport where ident = '{ICAO_code}'")
    result = cursor.fetchone()
    if result:     # jos ei ole lopputulosta = none = false
        return result
    else:
        return 'Ei löydyy'

ICAO = input('Anna lentoaseman ICAO-koodin: ')
while ICAO != '':
    lopputulos = get_airport_by_icao_code(ICAO)
    if lopputulos == 'Ei löydyy':
        print(lopputulos)
    else:
        print(f'{ICAO} - koodilla löytyy "{lopputulos[0]}" kaupungissa: {lopputulos[1]} \n')
    ICAO = input('Anna lentoaseman ICAO-koodin: ')

print('Moro!')