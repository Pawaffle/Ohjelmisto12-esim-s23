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

viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")