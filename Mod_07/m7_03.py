airports = {}

########################################################################################

def delete():
    print('perkele')

def add():
    ICAO = input('Anna ICAO koodin: ')
    airport_name = input('Anna lentoaseman nimen: ')
    airports[ICAO] = airport_name

def find():
    number = input('mikä nimi haluat poista?: ')
    if number in airports:
        airports.remove(number)
        print(number, 'on poistettu')
    else:
        print('Sellaista nimea ei löyty')

def commands():
    command = ['', 'Add', 'Find', 'Delete', 'Exit']
    for i, c in enumerate(command):
        if i > 0:
            print(f'{i}) {c}')

########################################################################################

print(f'''Terve!
  Tämä ohjelma tarkotettu lentoasematietojen hakemiseksi ja tallentamiseksi.
  Sinulla olemassa seuravat vaihtoehdot:''')

commands()
number = input('\nAnna sopivan komennon numero: ')
print()

while number  != '4':

    if number == '1':
        add()
    elif number == '2':
        find()
    elif number == '3':
        delete()
    elif number == 'lista':
        for i in airports:
            print(f'{i} - {airports[i]}')

    commands()
    number = input('\nAnna sopivan komennon numero: ')
    print()

'''
print(f'Sinä olet lisännyt {len(airports)} nimea.')
print(f'Tässä ne on: {(airports)}')
'''