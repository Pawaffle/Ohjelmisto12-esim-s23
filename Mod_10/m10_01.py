import time


def slow_print(text):
    for x in text:
        print(x, end='', flush=True)
        time.sleep(0.1)


class Hissi:

    def __init__(self, alla, ylla):
        self.alakerros = alla
        self.ylakerros = ylla
        self.kerros = alla

    def kerros_ylos(self):
        self.kerros += 1
    def kerros_alas(self):
        self.kerros -= 1
    def siirry_kerroksen(self, target):
        while self.kerros != target:
            if self.kerros < target:
                self.kerros_ylos()
                print(self.kerros)
                time.sleep(0.02)
            else:
                self.kerros_alas()
                print(self.kerros)
                time.sleep(0.02)

        print(f'Onittelut! Olet {self.kerros}:saa')



slow_print('Tervetuloa hissin \n')
slow_print('Anna alin kerros')
alin = int(input(' :'))
slow_print('Anna ylin kerros')
ylin = int(input(' :'))

h = Hissi(alin, ylin)

while True:
    slow_print(f'Olet {h.kerros}:ssa. Mihin haluat?\n')
    kerros = int(input('>'))

    while kerros not in range(alin, (ylin+1)):
        slow_print('\nSellaista ei ole, yrita uudelleen')
        kerros = int(input(' :'))

    h.siirry_kerroksen(kerros)


