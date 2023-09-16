minun_lista = [1, 2, 3, 4, 5, 6]

minun_monikko = (1, 2, 3, 4, 5, 6)

minun_monikko2 = 1, 2, (3, 4), 5, 6

minun_string = '123456'


# listan voi muokata
minun_lista [0] = 0
print(minun_lista)

# muut ei saa
# minun_monikko[0] != 0
print(minun_monikko[0])

minun_set = {'Monopoly', 'Shakki', 'Cluedo'}
print(minun_set)

minun_set.add('Riski')
print(minun_set)


# sanakirja
########################

oppilat = {'Aapeli': 25, 'Bertta': 45, 'Cecilia': 16}

# avaimet
for i in oppilat:
    print(i)

print()

# arvot
for i in oppilat:
    print(oppilat[i])

print()

# tiettuet - items
print(oppilat.items())

print(oppilat.keys())
print(oppilat.values())

oppilat['aaa'] = 10
# del oppilat['aaa']
numero_talteen = oppilat.pop('aaa')
print(numero_talteen)


'''

def main():
    months = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu",
              "lokakuu", "marraskuu", "joulukuu")
    seasons = ("talvikuukasi", "kevätkuukausi", "kesäkuukausi", "syyskuukausi")
    print("Valitse monesko kuukausi:")

mii(['hello world','hello','hello cat','hellolot of cats']) == {'hello': {0, 1, 2},
                                                                'cat': {2},
                                                                'of': {3},
                                                                'world': {0},
                                                                'cats': {3},
                                                                'hellolot': {3}}
'''