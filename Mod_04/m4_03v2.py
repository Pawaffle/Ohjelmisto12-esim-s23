print('Ohjelma tulostaa saaduista luvuista pienimmän ja suurimman')
print('Jos annat jotain paitsi lukua - ohjelma lopettaa toimintansa \n')

var = input('Anna joku luku: ')

# merkkien jono lataan "[...]"
merkkijen_jono = []

while True:
    try:
        float(var)
        # append = lisays
        merkkijen_jono.append(var)
        var = input('Anna seurava luku: ')
    except Exception:
        break

print(f'''
{min(merkkijen_jono)} - on pienin sinun luvuista
{max(merkkijen_jono)} - on isoin sinun luvuista ''')