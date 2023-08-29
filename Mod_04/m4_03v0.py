print('Ohjelma tulostaa saaduista luvuista pienimmän ja suurimman')
print('Jos painat enteria ilman lukua - ohjelma lopettaa toimintansa \n')

var = input('Anna joku luku: ')
min = max = var

while var != '':

    var = float(var)
    min = float(min)
    max = float(max)

    if var < min:
        min = var

    if var > max:
        max = var

    var = input('Anna seurava luku: ')

print(f'''
{min} - on pienin sinun luvuista
{max} - on isoin sinun luvuista ''')