'''
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina
annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä
talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. Kirjoita
taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita
pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
'''

raput = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']


import time

def screen_refresh():
    print('\n' * 20)

def slow_print(text):
    for x in text:
        print(x, end='', flush=True)
        #time.sleep(0.1)

class Talo:

    hissit = {}
    def __init__(self, alla, ylla, h_määrä):
        self.alakerros = alla
        self.ylakerros = ylla
        for x in range (h_määrä):
            h_name = 'hissi ' + raput[x]
            hissi = Hissi(alla, ylla, h_name)
            self.hissit[h_name] = hissi


    def aja_hissia(self, hissin_nimi, target):
        self.hissin_nimi.siirry_kerrokseen(target)


class Hissi:

    def __init__(self, alla, ylla, h_nimi):
        self.alakerros = alla
        self.ylakerros = ylla
        self.kerros = alla
        self.nimi = h_nimi

    def kerros_ylos(self):
        self.kerros += 1
    def kerros_alas(self):
        self.kerros -= 1
    def siirry_kerroksen(self, target):
        while self.kerros != target:
            if self.kerros < target:
                self.kerros_ylos()
                print(self.kerros)
                #time.sleep(0.02)
            else:
                self.kerros_alas()
                print(self.kerros)
                #time.sleep(0.02)

        print(f'Onittelut! Olet {self.kerros}:saa')
        time.sleep(1)



slow_print('Tehdään talo \n')
slow_print('Anna alin kerros')
alin = int(input(' : '))
slow_print('Anna ylin kerros')
ylin = int(input(' : '))
slow_print('Anna hissien määrä')
h_luku = int(input(' : '))

t = Talo(alin, ylin, h_luku)

while True:
    screen_refresh()
    print('*******************************************************************************')
    for hissi in t.hissit:
        print(f'{t.hissit[hissi].nimi} rapussa, sijaitsee kerroksessa {t.hissit[hissi].kerros}')
    print('******************************************************************************* \n')

    slow_print(f'Mikä hissi halua ajaa? ')
    toivo = "hissi " + input(' : ')

    while toivo not in t.hissit:
        slow_print('\nSellaista ei ole, yrita uudelleen')
        toivo = "hissi " + input(' : ')


    slow_print(f'Olet {t.hissit[toivo].kerros}:ssa. Mihin haluat?')
    kerros = int(input(' : '))

    while kerros not in range(alin, (ylin+1)):
        slow_print('\nSellaista ei ole, yrita uudelleen')
        kerros = int(input(' : '))

    t.hissit[toivo].siirry_kerroksen(kerros)
