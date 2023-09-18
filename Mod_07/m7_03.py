airports = {}


########################################################################################

def delete():
    poistava = input('Mitä haluat poista? Anna ICAO koodin: ')
    if poistava in airports:
        talteen = airports.pop(poistava)
        # del airports[poistava]
        print(f'{poistava}-{talteen} poistettu')
    else:
        print(f'Lentoasem {poistava} Ei löydyy')


def add():
    ICAO = input('Anna ICAO koodin: ')
    airport_name = input('Anna lentoaseman nimen: ')
    airports[ICAO] = airport_name


def find():
    lento = input('Mitä asema olet etsimässä? Anna ICAO: ')
    print(airports.get(lento, 'EI LÖYDY'))


def list():
    for i in airports:
        print(f'{i} - {airports[i]}')


def commands():
    command = ['', 'Add', 'Find', 'Delete', 'List', 'Exit']
    print()
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

while number != '5':

    if number == '1':
        add()
    elif number == '2':
        find()
    elif number == '3':
        delete()
    elif number == '4':
        list()

    commands()
    number = input('\nAnna sopivan komennon numero: ')
    print()

print('Tässä on talennetut lentoasemat: ')
list()
print('Näkemiin')