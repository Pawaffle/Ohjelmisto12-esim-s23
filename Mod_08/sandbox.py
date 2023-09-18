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

print(yhteys)
'''
cursor = yhteys.cursor()
# cursor.execute("select iso_country, name from country where iso_country = 'FI'")
#cursor.execute("select iso_country, name from country")
#result = cursor.fetchall()  # voi olla fetchone
#print(cursor.rowcount)
# print(result)

cursor.execute("select iso_country, name from country")
result = cursor.fetchall()
# F = cursor.rowcount
# for i in range(247):
#     result = cursor.fetchone()
#     print(f'{i} - {result}')
print(cursor.rowcount)
for country in result:
    print(f'1 - {country[1]}, ja sen koodi on {country[0]}')
'''
#
# country = get_country_by_iso_code('FI')
# print(country[1])
# country = get_country_by_iso_code('qwerty')
# print(country)

def get_country_by_iso_code(iso_code):
    cursor = yhteys.cursor()
    cursor.execute(f"select iso_country, name from country where iso_country = '{iso_code}'")
    result = cursor.fetchone()
    if result:    # jos ei ole lopputulosta = none = false
        return result
    else:
        return 'Ei löydyy'

def update_country_by_iso_code(iso_code, country_name):
    cursor = yhteys.cursor()
    sql = (f"update country set name='{country_name}' where iso_country = '{iso_code}'")
    cursor.execute(sql)
    print(cursor.rowcount)

haku = input('Anna etsiman maan koodi koodi > ')

while haku != '':
    country = get_country_by_iso_code(haku)
    print(country)
    haku = input('Anna koodi > ')


country_code = input('Anna muokkavan maan koodi > ')
new_name = input('Anna uusi nimi > ')
update_country_by_iso_code(country_code, new_name)