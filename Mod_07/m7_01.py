kuu_kirja = {"12": ("talvi", "joulukuu"),
           "1": ("talvi", "tammikuu"),
           "2": ("talvi", "helmikuu"),
           "3": ("kevät", "maaliskuu"),
           "4": ("kevät", "huhtikuu"),
           "5": ("kevät", "toukokuu"),
           "6": ("kesä", "kesäkuu"),
           "7": ("kesä", "heinäkuu"),
           "8": ("kesä", "elokuu"),
           "9": ("syksy", "syyskuu"),
           "10": ("syksy", "lokakuu"),
           "11": ("syksy", "marraskuu"), }

print('''Ohjelma tulostaa numeron vastaavan kuukauden ja vuodenajan
Ohjelman päätymiseen -  paina "Enter" ilman lukua
''')

i = input('Anna joku numero: ')

while i != '':
    vuoden_aika, kuukausi = kuu_kirja[i]
    print(f'{i}. Vastaava kuukausi on {kuukausi}, se on {vuoden_aika} \n')
    i = input('Anna seurava numero: ')

print('Näkemiin!')