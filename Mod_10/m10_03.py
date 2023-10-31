import time, random
raput = ['a', 'b', 'c', 'd', 'e', 'f']

def screen_refresh():
    print('\n' * 20)

def kowalsky_report():
    r = 0
    print('*******************************************************************************')
    for hissi in t.hissit:
        print(f'hissi {raput[r]} rapussa, sijaitsee kerroksessa {hissi.kerros}')
        r += 1
    print('******************************************************************************* \n')

def report():
    print()
    var = t.__dict__
    for x in var:
        print(f'{x} : {var[x]}')

    print()
    var = t.hissit
    for elev in var:
        x = elev.__dict__
        print(f"Elevator {raput[elev.nimi]} dictionary ahead -->")
        for record in x:
            print(f'{record} : {x[record]}')
        print(" ")

def allarm():
    for hissi in t.hissit:
        hissi.siirry_kerroksen(t.alakerros)

class Talo:

    def __init__(self, alla, ylla, h_määrä):
        self.alakerros = alla
        self.ylakerros = ylla
        self.hissit = []
        for x in range (h_määrä):
            h_name = x
            hissi = Hissi(alla, ylla, h_name)
            self.hissit.append(hissi)


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

        print(f'Onittelut! Olet {self.kerros}:saa \n')

def main():
    global t
    t = Talo(alin_kerros, ylin_kerros, hissien_määrä)

    i = 0
    while i < pelin_toistoen_määrä:
        i += 1

        kowalsky_report()

        h = random.randint(0, 4)
        k = random.randint(0, 10)

        print(f'Siiretään {raput[h]} rapussa oleva hissi - {k} kerrokseen')

        time.sleep(3)

        screen_refresh()
        t.hissit[h].siirry_kerroksen(k)

    kowalsky_report()

    alarm = input('Paina "y" ja "ENTER" jos haluat palohälytyksen :')
    if alarm == 'y':
        allarm()
        kowalsky_report()

    rakenne = input('Paina "y" ja "ENTER" jos haluat nähdä olioden rakenne :')
    if rakenne == 'y':
        report()




##### Asetukset ##############

alin_kerros = 0
ylin_kerros = 10
hissien_määrä = 5
pelin_toistoen_määrä = 10

###############################
main()