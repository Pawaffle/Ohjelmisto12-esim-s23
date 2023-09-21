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
##################################################################################################
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa 
olevien LENTOKENTTIEN LUKUMÄÄRÄT TYYPEITÄIN. Esimerkiksi Suomen osalta tuloksena on saatava 
tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.
##################################################################################################
'''
#select type, count(*) from airport where iso_country = 'FI' group by type;

def get_airports_by_country_code(code):
    cursor = yhteys.cursor()
    cursor.execute(f"select type, count(*) from airport where iso_country = '{code}' group by type;")
    result = cursor.fetchall()
    if result:     # jos ei ole lopputulosta = none = false
        return result
    else:
        return 'Ei löydyy'


XX = input('\nAnna maakoodin (esimerkiksi FI): ')
while XX != '':
    lopputulos = get_airports_by_country_code(XX)
    if lopputulos == 'Ei löydyy':
        print(lopputulos)
    else:
        for i in lopputulos:
            print(f' - {i[0]} - {i[1]}')
    XX = input('\nAnna maakoodin (esimerkiksi FI): ')

print('Moro!')