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


alin = 0
ylin = 10
h_luku = 5

t = Talo(alin, ylin, h_luku)
print(t.__dict__)

i = 0
while i < 10:
    i += 1

    kowalsky_report()

    h = random.randint(0, 4)
    k = random.randint(0, 10)

    print(f'Siiretään {raput[h]} rapussa oleva hissi - {k} kerrokseen')

    time.sleep(3)

    screen_refresh()
    t.hissit[h].siirry_kerroksen(k)

kowalsky_report()
