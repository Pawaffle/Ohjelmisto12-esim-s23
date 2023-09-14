nimet = set()

i = len(nimet)
nimi = input('Anna joku nimi: ')

while nimi != '':

    nimet.add(nimi)
    if i == len(nimet):
        print('Lisatty ajemmin')
    else:
        print('Uusi nimi')

    i = len(nimet)
    nimi = input('\nAnna seurava nimi: ')

print('\nOlet lisännyt seuravat nimet:')
for i in nimet:
    print(f'- {i}')