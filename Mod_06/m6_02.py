import random


def noppan_heitto(maksimi_arvo):
    x = random.randint(1, maksimi_arvo)
    return x

arvo = int(input('Anna nopan tahkojen yhteismäärä: '))
#muutetan arvo posiitiveksi jos se on annettu negatiivena
arvo = int((arvo*arvo) ** 0.5)

num = 0
while num != arvo:
    num = noppan_heitto(maksimi_arvo=arvo)
    print(num)