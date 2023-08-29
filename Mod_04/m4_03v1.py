print('Ohjelma tulostaa saaduista luvuista pienimmän ja suurimman')
print('Jos annat jotain paitsi numeroa - ohjelma lopettaa toimintansa \n')

var = float(input('Anna joku luku: '))
min = max = var

while True:
    try:

        if var < min:
            min = var

        if var > max:
            max = var

        var = float(input('Anna seurava luku: '))
    except Exception:
        break


print(f'''
{min} - on pienin sinun luvuista
{max} - on isoin sinun luvuista ''')