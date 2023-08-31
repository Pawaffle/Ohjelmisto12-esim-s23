
name_list = []

nimi = input('Anna joku nimi: ')

while nimi  != '':

    if nimi == 'poista':
        nimi = input('mikä nimi haluat poista?: ')
        if nimi in name_list:
            name_list.remove(nimi)
            print(nimi, 'on poistettu')
        else:
            print('Sellaista nimea ei löyty')
    elif nimi == 'lista':
        for nimi in name_list:
            print(f'--- {nimi} ---')
    else:
        name_list.append(nimi)
    nimi = input('Seurava nimi / "poista" / "lista" : ')

print(f'Sinä olet lisännyt {len(name_list)} nimea.')
print(f'Tässä ne on: {(name_list)}')
